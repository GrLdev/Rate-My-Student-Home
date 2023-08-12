from app import app, db
from flask import render_template, url_for, redirect, request, jsonify, flash
from app.forms import CreateReviewForm, SearchForm, SortForm
from app.models import Review, Property, House, Halls, EstateAgent, User
from secret_keys import google_maps_api_key
from sqlalchemy import or_

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/review', methods=['GET', 'POST'])
@app.route('/review/', methods=['GET', 'POST'])
def review():
    form = SearchForm()
    if form.validate_on_submit():
        sort_form = SortForm()
        search_type = form.search_type.data
        reviews = []
        location = None

        if search_type == "address":
            ### code to search for both halls and houses
            # property = Property.query.filter(
            #     or_(Property.address.ilike(f'{form.search_address.data}%'), Property.address.ilike(f'% {form.search_address.data}%'))
            # ).order_by(
            #     Property.address.ilike(f'{form.search_address.data}%').desc(),
            #     Property.address.ilike(f'%{form.search_address.data}%').desc()
            # ).first()
            property = Property.query.join(House).filter(
                or_(Property.address.ilike(f'{form.search_address.data}%'), Property.address.ilike(f'% {form.search_address.data}%'))
            ).order_by(
                Property.address.ilike(f'{form.search_address.data}%').desc(),
                Property.address.ilike(f'%{form.search_address.data}%').desc(),
                Property.address
            ).first()
            if property:
                location = property.address
                reviews = Review.query.filter_by(property_id=property.id).all()
                current_rent = property.associated_house[0].rent

        elif search_type == "halls":
            property = Property.query.join(Halls).filter(
                or_(Property.address.ilike(f'{form.search_address.data}%'), Property.address.ilike(f'% {form.search_address.data}%'))
            ).order_by(
                Property.address.ilike(f'{form.search_address.data}%').desc(),
                Property.address.ilike(f'%{form.search_address.data}%').desc(),
                Property.address
            ).first()
            if property:
                location = property.address
                reviews = Review.query.filter_by(property_id=property.id).all()
                current_rent = property.associated_halls[0].rent

        elif search_type == "agent":
            agent = EstateAgent.query.filter(
                or_(EstateAgent.name.ilike(f'{form.search_address.data}%'), EstateAgent.name.ilike(f'% {form.search_address.data}%'))
            ).order_by(
                EstateAgent.name.ilike(f'{form.search_address.data}%').desc(),
                EstateAgent.name.ilike(f'%{form.search_address.data}%').desc(),
                EstateAgent.name
            ).first()
            if agent:
                location = agent.name
                reviews = Review.query.filter_by(estate_agent_id=agent.id).all()
                current_rent = None

        return render_template('search.html', title='Search', form=form, reviews=reviews, location=location, sort_form=sort_form, current_rent=current_rent)
    
    return render_template('review.html', title='Review', form=form)

@app.route('/autocomplete-address')
def autocomplete():
    term = request.args.get('term', '')
    ### code to search for both halls and houses
    # addresses = Property.query.filter(Property.address.ilike(f'{term}%')).order_by(
    #     Property.address.ilike(f'{term}%').desc(),
    #     Property.address.ilike(f'%{term}%').desc()
    # ).limit(10).all()
    addresses = Property.query.join(House).filter(
        or_(Property.address.ilike(f'{term}%'), Property.address.ilike(f'% {term}%'))
    ).order_by(
        Property.address.ilike(f'{term}%').desc(),
        Property.address.ilike(f'%{term}%').desc(),
        Property.address
    ).limit(10).all()
    address_list = [address.address for address in addresses]
    return jsonify({'addresses': address_list})

@app.route('/autocomplete-halls')
def autocomplete_halls():
    term = request.args.get('term', '')
    if term.strip() == '':
        properties = Property.query.join(Halls).order_by(Property.address).all()
    else:
        properties = Property.query.join(Halls).filter(
            or_(Property.address.ilike(f'{term}%'), Property.address.ilike(f'% {term}%'))
        ).order_by(
            Property.address.ilike(f'{term}%').desc(),
            Property.address.ilike(f'%{term}%').desc(),
            Property.address
        ).all()
    address_list = [property.address for property in properties]
    return jsonify({'addresses': address_list})
    
@app.route('/autocomplete-agent')
def autocomplete_agent():
    term = request.args.get('term', '')
    if term.strip() == '':
        agents = EstateAgent.query.order_by(EstateAgent.name).all()
    else:
        agents = EstateAgent.query.filter(
            or_(EstateAgent.name.ilike(f'{term}%'), EstateAgent.name.ilike(f'% {term}%'))
        ).order_by(
            EstateAgent.name.ilike(f'{term}%').desc(),
            EstateAgent.name.ilike(f'%{term}%').desc(),
            EstateAgent.name
        ).all()
    agent_list = [agent.name for agent in agents]
    return jsonify({'agents': agent_list})

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
            review = Review(user_id=user.id, property_id=property.id, estate_agent_id=form.letting_agent.data, overall_rating=form.overall_rating.data, condition_rating=form.condition_rating.data, security_rating=form.security_rating.data, landlord_rating=form.landlord_rating.data, comment=form.review.data, rent=form.rent.data)
            
        elif form.home_type.data == 'halls':
            hall = Halls.query.filter_by(id=form.hall.data).first()
            property_id = hall.property_id
            review = Review(user_id=user.id, property_id=property_id, estate_agent_id="none", overall_rating=form.overall_rating.data, condition_rating=form.condition_rating.data, security_rating=form.security_rating.data, landlord_rating=form.landlord_rating.data, comment=form.review.data, rent=form.rent.data)

        db.session.add(review)
        db.session.commit()

        return render_template('confirm.html', title='Confirm')
    
    for error in form.errors:
        flash(error, 'danger')
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
            avg_rating = round(avg_rating, 2)

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