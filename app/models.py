from app import db
from datetime import datetime

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

    def __repr__(self):
        return f"Review(id='{self.id}', user_id='{self.user_id}', property_id='{self.property_id}', estate_agent_id='{self.estate_agent_id}', overall_rating='{self.overall_rating}', condition_rating='{self.condition_rating}', security_rating='{self.security_rating}', landlord_rating='{self.landlord_rating}', date='{self.date}', comment='{self.comment}')" 

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(256), nullable=False)
    reviews = db.relationship('Review', backref='property', lazy=True)

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    rent = db.Column(db.Integer, nullable=False)

class Halls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    rent = db.Column(db.Integer, nullable=False)
    
class EstateAgent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(256), nullable=False)
    website = db.Column(db.String(256), nullable=False)
    reviews = db.relationship('Review', backref='estate_agent')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    university = db.Column(db.String(256), nullable=False)