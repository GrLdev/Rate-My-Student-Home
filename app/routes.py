from app import app, db
from flask import render_template
from app.forms import CreateReviewForm
from app.models import Review, Property, House, Halls, EstateAgent, User
from secret_keys import google_maps_api_key

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
            existing_property = Property.query.filter_by(lat=form.lat, lng=form.lng).first()
            
            if existing_property:
                property = existing_property
            else:
                property = Property(lat=form.lat, lng=form.lng, address=address)
                db.session.add(property)
                db.session.commit()
                house = House(property_id=property.id, bedrooms=form.bedrooms.data, bathrooms=form.bathrooms.data, rent=form.rent.data)
                db.session.add(house)
            review = Review(user_id=user.id, property_id=property.id, estate_agent_id=form.letting_agent.data, overall_rating=form.overall_rating.data, condition_rating=form.condition_rating.data, security_rating=form.security_rating.data, landlord_rating=form.landlord_rating.data, comment=form.review.data)

        elif form.home_type.data == 'halls':
            hall = Halls.query.filter_by(id=form.hall.data).first()
            property_id = hall.property_id
            review = Review(user_id=user.id, property_id=property_id, estate_agent_id="none", overall_rating=form.overall_rating.data, condition_rating=form.condition_rating.data, security_rating=form.security_rating.data, landlord_rating=form.landlord_rating.data, comment=form.review.data)

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
    property_location_data = {}
    properties = Property.query.all()
    
    for property in properties:

        reviews = Review.query.filter_by(property_id=property.id).all()
        avg_rating = 0
        if len(reviews) != 0:
            for review in reviews:
                avg_rating += review.overall_rating
            avg_rating /= len(reviews)

        houses = House.query.filter_by(property_id=property.id).all()
        halls = Halls.query.filter_by(property_id=property.id).all()
        if houses:
            rent = houses[0].rent
        elif halls:
            rent = halls[0].rent
        else:
            rent = 0
        rent = rent/100

        property_location_data[property.id] = {
            "coords" : [property.lat, property.lng],
            "address" : property.address,
            "avg_rating" : avg_rating,
            "rent" : rent,
        }
    return render_template('map.html', title='Map', property_location_data=property_location_data, google_maps_api_key=google_maps_api_key)