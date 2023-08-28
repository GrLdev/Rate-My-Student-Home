from app import db, login_manager, app
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import event
from queue import Queue
import threading

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    estate_agent_id = db.Column(db.Integer, db.ForeignKey('estate_agent.id'))
    overall_rating = db.Column(db.Integer, nullable=False)
    condition_rating = db.Column(db.Integer, nullable=False)
    security_rating = db.Column(db.Integer, nullable=False)
    landlord_rating = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    comment = db.Column(db.String(1000), nullable=False)
    removed = db.Column(db.Boolean, nullable=False, default=False)
    reports = db.relationship('Report', backref='review', lazy=True)
    rent = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Review(id='{self.id}', user_id='{self.user_id}', property_id='{self.property_id}', estate_agent_id='{self.estate_agent_id}', overall_rating='{self.overall_rating}', condition_rating='{self.condition_rating}', security_rating='{self.security_rating}', landlord_rating='{self.landlord_rating}', date='{self.date}', comment='{self.comment}')" 

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(256), nullable=False)
    reviews = db.relationship('Review', backref='property', lazy=True)
    associated_house = db.relationship('House', back_populates='property', lazy=True, overlaps='associated_house, associated_property')
    associated_halls = db.relationship('Halls', back_populates='property', lazy=True, overlaps='associated_halls, associated_property')

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    rent = db.Column(db.Integer, nullable=False)
    property = db.relationship('Property', back_populates='associated_house', lazy=True, uselist=False, overlaps='associated_house, associated_property')

class Halls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    rent = db.Column(db.Integer, nullable=False)
    property = db.relationship('Property', back_populates='associated_halls', lazy=True, uselist=False, overlaps='associated_halls, associated_property')

class EstateAgent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(256), nullable=False)
    website = db.Column(db.String(256), nullable=False)
    reviews = db.relationship('Review', backref='estate_agent')
    requests = db.relationship('EstateAgentRequest', back_populates='estate_agent', lazy=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    university = db.Column(db.String(256), nullable=True)
    reports = db.relationship('Report', backref='user', lazy=True)
    estate_agent_requests = db.relationship('EstateAgentRequest', back_populates='user', lazy=True)

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable=False)
    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    handled = db.Column(db.Boolean, nullable=False, default=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    comment = db.Column(db.String(1000), nullable=False)

class EstateAgentRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    estate_agent_id = db.Column(db.Integer, db.ForeignKey('estate_agent.id'), nullable=True)
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(256), nullable=False)
    website = db.Column(db.String(256), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    handled = db.Column(db.Boolean, nullable=False, default=False)
    user = db.relationship('User', back_populates='estate_agent_requests', lazy=True)
    estate_agent = db.relationship('EstateAgent', back_populates='requests', lazy=True)

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

rent_updates_queue = Queue()

def update_rent_thread():
    while True:
        property_id, latest_rent = rent_updates_queue.get()
        with app.app_context():
            house_or_halls = (
                House.query.join(Review, House.property_id == Review.property_id)
                    .filter(House.property_id == property_id, Review.removed == False)
                    .order_by(Review.date.desc())
                    .first()
                or Halls.query.join(Review, Halls.property_id == Review.property_id)
                    .filter(Halls.property_id == property_id, Review.removed == False)
                    .order_by(Review.date.desc())
                    .first()
            )
            if house_or_halls:
                house_or_halls.rent = latest_rent
                db.session.commit()
        rent_updates_queue.task_done()

update_thread = threading.Thread(target=update_rent_thread)
update_thread.daemon = True
update_thread.start()

@event.listens_for(Review, 'after_insert')
@event.listens_for(Review, 'after_update')
def update_review_rent(mapper, connection, target):
    property_id = target.property_id
    if property_id:
        rent_updates_queue.put((property_id, target.rent))
