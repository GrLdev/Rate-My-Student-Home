from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField, IntegerRangeField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, Regexp
from app.maps import get_coords
from decimal import Decimal
from app.models import EstateAgent, Halls, Property

class PriceField(DecimalField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = int(Decimal(valuelist[0]) * 100)
            except (ValueError, TypeError):
                self.data = None
                raise ValueError(self.gettext('Invalid rent value'))

class CreateReviewForm(FlaskForm):
    # place_id = None
    lat = None
    lng = None

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
    university = RadioField("Which university do you belong to?", choices=[('cardiff_uni','Cardiff University'),('cardiff_met','Cardiff Metropolitan University'),('usw','University of South Wales')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=58)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=58)])
    email = StringField("Email", validators=[DataRequired()])
    accepted_terms = BooleanField("I accept the terms and conditions", validators=[DataRequired()])
    submit = SubmitField("Submit Review")

    def validate(self, extra_validators=None):
        try:
            if self.home_type.data == "house":
                combined_address = self.address_line_1.data + "+" + self.address_line_2.data + "+" + self.city.data + "+" + self.postcode.data
                self.lat, self.lng = get_coords(combined_address)
                if not self.lat or not self.lng:
                    raise ValidationError("Place ID is invalid, make sure you entered a valid address")

            return True
        
        except Exception as e:
            raise ValidationError(f"An error occurred: {e}")
        
