from app import app, db
from flask import render_template, url_for, redirect, request, jsonify, flash
from flask_login import current_user, login_user, logout_user, login_required
from secret_keys import google_maps_api_key
from sqlalchemy import or_
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import Review, Property, House, Halls, EstateAgent, User, Admin, Report, datetime
from app.forms import CreateReviewForm, SearchForm, SortForm, AdminLoginForm, ReportForm, RemoveReviewForm, BrowseTypeForm, SortByPropertyForm, SortByLandlordForm, FilterByRatingForm, FilterByRentForm, FilterByBedroomsForm, FilterByBathroomsForm
from datetime import timedelta
from sqlalchemy.orm import joinedload

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
                reviews = Review.query.filter_by(property_id=property.id, removed=False).all()
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
                reviews = Review.query.filter_by(property_id=property.id, removed=False).all()
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
                reviews = Review.query.filter_by(property_id=property.id, removed=False).all()
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
        existing_user = User.query.filter_by(email=form.email.data).first()

        if not existing_user:
            fullname = form.first_name.data + ' ' + form.last_name.data
            user = User(name=fullname, email=form.email.data, university=form.university.data)
            db.session.add(user)
            db.session.commit()
        else:
            user = existing_user
            reviews = Review.query.filter_by(user_id=user.id).all()
            for review in reviews:
                if datetime.now() - review.date < timedelta(minutes=1):        # change to a longer time period
                    flash('You have already submitted a review this week/month/year', 'danger')
                    return redirect(url_for('create'))
            
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

        reviews = Review.query.filter_by(property_id=property.id, removed=False).all()
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

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin and check_password_hash(admin.password, form.password.data):
            login_user(admin)
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    
    return render_template('admin-login.html', title='Admin Login', form=form)

@app.route('/admin-dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    form = RemoveReviewForm()
    unhandled_reports = Report.query.filter_by(handled=False).all()
    handled_reports = Report.query.filter_by(handled=True).all()
    
    if form.validate_on_submit():
        report = Report.query.filter_by(id=request.form["reported"]).first_or_404()
        review = Review.query.filter_by(id=report.review_id).first_or_404()

        if request.form["action"] == "remove":
            review.removed = True
            report.handled = True
            flash('Review removed', 'success')
        elif request.form["action"] == "ignore":
            report.handled = True
            flash('Review ignored', 'success')
        db.session.commit()
        return redirect(url_for('admin_dashboard'))
    return render_template('admin-dashboard.html', title='Admin Dashboard', unhandled_reports=unhandled_reports, handled_reports=handled_reports, form=form)

@app.route('/admin-logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))

@app.route('/report/<int:review_id>', methods=['GET', 'POST'])
def report(review_id):
    form = ReportForm()
    if Review.query.filter_by(id=review_id, removed=False).first():
        if form.validate_on_submit():
            fullname = form.first_name.data + ' ' + form.last_name.data
            user = User(name=fullname, email=form.email.data, university=form.university.data)
            db.session.add(user)
            db.session.commit()
            report = Report(review_id=review_id, reporter_id=user.id, comment=form.comment.data)
            db.session.add(report)
            db.session.commit()
            flash('Report submitted successfully', 'success')
            return redirect(url_for('home'))
    else:
        flash('Review does not exist', 'danger')
        return redirect(url_for('home'))
    return render_template('report.html', title='Report', form=form)

@app.route('/browse', methods=['GET', 'POST'])
@app.route('/browse/', methods=['GET', 'POST'])
def browse():
    browse_type_form = BrowseTypeForm()
    if browse_type_form.validate_on_submit():
        return browse_form_action(browse_type_form)
    return render_template('browse.html', title='Browse', browse_type_form=browse_type_form)

@app.route('/browse/house', methods=['GET', 'POST'])
def browse_house():
    browse_type_form = BrowseTypeForm()
    sort_by = SortByPropertyForm()
    filter_by_rating = FilterByRatingForm()
    filter_by_rent = FilterByRentForm()
    filter_by_bedrooms = FilterByBedroomsForm()
    filter_by_bathrooms = FilterByBathroomsForm()

    browse_type_form.browse_type.process(request.form, data='house')
    reviews = (Review.query.join(Property).filter(Review.property_id == Property.id).join(House).options(joinedload(Review.property)).filter(Review.removed == False).all())

    if browse_type_form.validate_on_submit():
        return browse_form_action(browse_type_form)
    
    return render_template('browse-category.html', title='Browse', browse_type_form=browse_type_form, sort_by=sort_by, reviews=reviews, browse_type='house', filter_by_rating=filter_by_rating, filter_by_rent=filter_by_rent, filter_by_bedrooms=filter_by_bedrooms, filter_by_bathrooms=filter_by_bathrooms)

@app.route('/browse/halls', methods=['GET', 'POST'])
def browse_halls():
    browse_type_form = BrowseTypeForm()
    sort_by = SortByPropertyForm()
    filter_by_rating = FilterByRatingForm()
    filter_by_rent = FilterByRentForm()

    browse_type_form.browse_type.process(request.form, data='halls')
    reviews = (Review.query.join(Property).filter(Review.property_id == Property.id).join(Halls).options(joinedload(Review.property)).filter(Review.removed == False).all())

    if browse_type_form.validate_on_submit():
        return browse_form_action(browse_type_form)
    
    return render_template('browse-category.html', title='Browse', browse_type_form=browse_type_form, sort_by=sort_by, reviews=reviews, browse_type='halls', filter_by_rating=filter_by_rating, filter_by_rent=filter_by_rent)

@app.route('/browse/landlord', methods=['GET', 'POST'])
def browse_landlord():
    browse_type_form = BrowseTypeForm()
    sort_by = SortByLandlordForm()
    filter_by_rating = FilterByRatingForm()

    browse_type_form.browse_type.process(request.form, data='landlord')
    reviews = (Review.query.join(EstateAgent).filter(Review.estate_agent_id == EstateAgent.id).options(joinedload(Review.estate_agent)).filter(Review.removed == False).all())

    if browse_type_form.validate_on_submit():
        return browse_form_action(browse_type_form)
    
    return render_template('browse-category.html', title='Browse', browse_type_form=browse_type_form, sort_by=sort_by, reviews=reviews, browse_type='landlord', filter_by_rating=filter_by_rating)

def browse_form_action(browse_type_form):
    if browse_type_form.browse_type.data == 'house':
        return redirect(url_for('browse_house'))
    elif browse_type_form.browse_type.data == 'halls':
        return redirect(url_for('browse_halls'))
    elif browse_type_form.browse_type.data == 'landlord':
        return redirect(url_for('browse_landlord'))
