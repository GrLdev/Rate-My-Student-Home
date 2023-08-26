from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField, IntegerRangeField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, Regexp
from app.maps import get_coords
from decimal import Decimal, InvalidOperation
from app.models import EstateAgent, Halls, Property

class PriceField(DecimalField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = int(Decimal(valuelist[0]) * 100)
            except InvalidOperation:
                self.data = None
                raise ValueError(self.gettext('Invalid rent value'))
        else:
            self.data = None

class CreateReviewForm(FlaskForm):
    # place_id = None
    lat = None
    lng = None
    errors = []

    # step 1
    home_type = RadioField("Do you live in a house or halls?", choices=[('house','House'),('halls','Halls')], validators=[DataRequired()], default='house')
    address_line_1 = StringField("Address Line 1", validators=[Length(min=2, max=94)])
    address_line_2 = StringField("Address Line 2", validators=[Length(max=94)])
    city = StringField("City", validators=[Length(min=2, max=58)])
    postcode = StringField("Postcode", validators=[Length(min=5, max=8), Regexp("([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})", message="Invalid postcode")])
    hall = SelectField("Halls", choices=[(hall.id, Property.query.filter_by(id=hall.property_id).first().address) for hall in Halls.query.all()])

    # step 2
    overall_rating = IntegerRangeField("Overall Rating", default=3 , validators=[DataRequired(), NumberRange(min=1, max=5)])
    condition_rating = IntegerRangeField("Condition Rating", default=3 , validators=[DataRequired(), NumberRange(min=1, max=5)])
    security_rating = IntegerRangeField("Security Rating", default=3 , validators=[DataRequired(), NumberRange(min=1, max=5)])
    landlord_rating = IntegerRangeField("Landlord Rating", default=3 , validators=[DataRequired(), NumberRange(min=1, max=5)])
    letting_agent = SelectField("Letting Agent", choices=[('none','None/Other')] + [(agent.id, agent.name) for agent in EstateAgent.query.all()])
    rent = PriceField("Rent £", validators=[DataRequired(), NumberRange(min=0, max=10000)])
    bedrooms = IntegerField("Bedrooms", default=1 , validators=[DataRequired(), NumberRange(min=1, max=10)])
    bathrooms = IntegerField("Bathrooms", default=1 , validators=[DataRequired(), NumberRange(min=1, max=10)])
    review = TextAreaField("Review", validators=[DataRequired(), Length(min=150, max=1000)])

    # step 3
    university = RadioField("Which university do you belong to?", choices=[('cardiff_uni','Cardiff University'),('cardiff_met','Cardiff Metropolitan University'),('usw','University of South Wales')], validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=58)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=58)])
    email = StringField("Email", validators=[DataRequired()])
    accepted_terms = BooleanField("I accept the terms and conditions", validators=[DataRequired()])
    submit = SubmitField("Submit Review")

    def validate(self, extra_validators=None):
        self.errors.clear()
        try:
            if self.home_type.data == "house":
                combined_address = self.address_line_1.data + "+" + self.address_line_2.data + "+" + self.city.data + "+" + self.postcode.data
                result = get_coords(combined_address)
                if not result:
                    raise ValidationError("Something went wrong internally")
                elif isinstance(result, str):
                    raise ValidationError(result)
                else:
                    self.lat, self.lng = result 

            return True
        
        except Exception as e:
            self.errors.append(str(e))
            return False
        
class SearchForm(FlaskForm):
    search_type = RadioField("Search Type", choices=[('address','Address'),('halls','Halls'),('agent','Letting Agent')], validators=[DataRequired()], default='address')
    search_address = StringField("Search", validators=[DataRequired()], id="search-input")
    submit = SubmitField("Search")

class SortForm(FlaskForm):
    sort_by = SelectField("Sort By", choices=[('recent','Most Recent'),('oldest','Oldest'),('overall_high','Overall Rating (highest first)'),('overall_low','Overall Rating (lowest first)')], validators=[DataRequired()], default='recent', id="sort-input")

class AdminLoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class ReportForm(FlaskForm):
    university = RadioField("Which university do you belong to?", choices=[(None,'None'),('cardiff_uni','Cardiff University'),('cardiff_met','Cardiff Metropolitan University'),('usw','University of South Wales')], validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=58)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=58)])
    email = StringField("Email", validators=[DataRequired()])
    comment = TextAreaField("Comment", validators=[DataRequired(), Length(min=10, max=1000)])
    submit = SubmitField("Report Review")

class RemoveReviewForm(FlaskForm):
    action = SelectField('Action', choices=[('remove', 'Remove'), ('ignore', 'Ignore')])
    submit = SubmitField('Handle')
    
class BrowseTypeForm(FlaskForm):
    browse_type = SelectField("Filter By", choices=[('house','House'),('halls','Halls'),('landlord','Landlord')], validators=[DataRequired()], default='house', render_kw={"onchange": "this.form.submit()"})

class SortByPropertyForm(FlaskForm):
    sort_by = SelectField("Sort By", choices=[('overall_high','Overall Rating (highest first)'),('overall_low','Overall Rating (lowest first)'),('recent','Most Recent'),('oldest','Oldest'),('rent_high','Rent (highest first)'),('rent_low','Rent (lowest first)')], validators=[DataRequired()], default='overall_high', id="sort-input")

class SortByLandlordForm(FlaskForm):
    sort_by = SelectField("Sort By", choices=[('overall_high','Overall Rating (highest first)'),('overall_low','Overall Rating (lowest first)'),('recent','Most Recent'),('oldest','Oldest')], validators=[DataRequired()], default='overall_high', id="sort-input")

class FilterByRatingForm(FlaskForm):
    filter_by = SelectField("Overall rating above", choices=[(5,'5'),(4,'4'),(3,'3'),(2,'2'),(1,'1')], validators=[DataRequired()], default='overall_5', id="filter-input")

class FilterByRentForm(FlaskForm):
    rent_min = PriceField("Min Rent £", validators=[DataRequired(), NumberRange(min=0, max=10000)], id="rent-min-input")
    rent_max = PriceField("Max Rent £", validators=[DataRequired(), NumberRange(min=0, max=10000)], id="rent-max-input")

class FilterByBedroomsForm(FlaskForm):
    bedrooms_min = SelectField("Min Bedrooms", choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10+','10+')], validators=[DataRequired()], default='1', id="bedrooms-min-input")
    bedrooms_max = SelectField("Max Bedrooms", choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10+','10+')], validators=[DataRequired()], default='10+', id="bedrooms-max-input")

class FilterByBathroomsForm(FlaskForm):
    bathrooms_min = SelectField("Min Bathrooms", choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[DataRequired()], default='1', id="bathrooms-min-input")
    bathrooms_max = SelectField("Max Bathrooms", choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[DataRequired()], default='10+', id="bathrooms-max-input")
    
class EstateAgentRequestForm(FlaskForm):
    name = StringField("Estate Agent Name", validators=[DataRequired(), Length(min=2, max=58)])
    agent_email = StringField("Estate Agent Email", validators=[DataRequired()])
    phone = StringField("Estate Agent Phone", validators=[DataRequired()])
    website = StringField("Estate Agent Website", validators=[DataRequired()])

    university = RadioField("Which university do you belong to?", choices=[('cardiff_uni','Cardiff University'),('cardiff_met','Cardiff Metropolitan University'),('usw','University of South Wales')], validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=58)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=58)])
    user_email = StringField("Email", validators=[DataRequired()])

    submit = SubmitField("Submit Request")

class RequestHandleForm(FlaskForm):
    action = SelectField('Action', choices=[('accept', 'Accept'), ('reject', 'Reject')])
    submit = SubmitField('Handle')