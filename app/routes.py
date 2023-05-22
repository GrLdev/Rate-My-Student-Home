from app import app, db
from flask import render_template
from app.forms import CreateReviewForm
from app.models import Review, Property, House, Halls, EstateAgent, User

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/review')
@app.route('/review/')  
def review():
    return render_template('review.html', title='Review')

@app.route('/review/create', methods=['GET', 'POST'])
def create():
    form = CreateReviewForm()
    if form.validate_on_submit():
        fullname = form.first_name.data + ' ' + form.last_name.data
        user = User(name=fullname, email=form.email.data, university=form.university.data)
        db.session.add(user)
        db.session.commit()
        if form.home_type.data == 'house':
            address = form.address_line_1.data + (', ' + form.address_line_2.data if form.address_line_2.data else '') + ', ' + form.city.data + ', ' + form.postcode.data
            property = Property(lat=form.lat, lng=form.lng, address=address)
            db.session.add(property)
            db.session.commit()

            house = House(property_id=property.id, bedrooms=form.bedrooms.data, bathrooms=form.bathrooms.data, rent=form.rent.data)
            db.session.add(house)
            review = Review(user_id=user.id, property_id=property.id, estate_agent_id=form.letting_agent.data, overall_rating=form.overall_rating.data, condition_rating=form.condition_rating.data, security_rating=form.security_rating.data, landlord_rating=form.landlord_rating.data, comment=form.review.data)

        elif form.home_type.data == 'halls':
            hall = Halls.query.filter_by(id=form.hall.data).first()
            property_id = hall.property_id
            review = Review(user_id=user.id, property_id=property_id, estate_agent_id=form.letting_agent.data, overall_rating=form.overall_rating.data, condition_rating=form.condition_rating.data, security_rating=form.security_rating.data, landlord_rating=form.landlord_rating.data, comment=form.review.data)

        db.session.add(review)
        db.session.commit()

        return render_template('confirm.html', title='Confirm')
    return render_template('create.html', title='Create Review', form=form)

@app.route('/help-center')
def help():
    return render_template('help.html', title='Help Center')

@app.route('/confirm')
def confirm():
    return render_template('confirm.html', title='Confirm')

@app.route('/map')
def map():
    return render_template('map.html', title='Map')