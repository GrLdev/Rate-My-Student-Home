from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField, IntegerRangeField, DecimalRangeField
from wtforms.validators import DataRequired, Length, NumberRange

class CreateReviewForm(FlaskForm):
    # step 1
    home_type = RadioField("Do you live in a house or halls?", choices=[('house','House'),('halls','Halls')])
    address_line_1 = StringField("Address Line 1", validators=[DataRequired(), Length(min=2, max=94)])
    address_line_2 = StringField("Address Line 2", validators=[DataRequired(), Length(min=2, max=94)])
    city = StringField("City", validators=[DataRequired(), Length(min=2, max=58)])
    postcode = StringField("Postcode", validators=[DataRequired(), Length(min=2, max=10)])

    # step 2
    overall_rating = IntegerRangeField("Overall Rating", default=2 , validators=[DataRequired(), NumberRange(min=0, max=4)])
    condition_rating = IntegerRangeField("Condition Rating", default=2 , validators=[DataRequired(), NumberRange(min=0, max=4)])
    security_rating = IntegerRangeField("Security Rating", default=2 , validators=[DataRequired(), NumberRange(min=0, max=4)])
    landlord_rating = IntegerRangeField("Landlord Rating", default=2 , validators=[DataRequired(), NumberRange(min=0, max=4)])
    letting_agent = SelectField("Letting Agent", choices=[('none','None'),('2let2','2Let2'),('student_cribs','Student Cribs'),('unite_students','Unite Students')])
    review = TextAreaField("Review", validators=[DataRequired(), Length(min=2, max=1000)])

    # step 3
    university = RadioField("Which university do you belong to?", choices=[('cardiff_uni','Cardiff University'),('cardiff_met','Cardiff Metropolitan University'),('usw','University of South Wales')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=58)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=58)])
    email = StringField("Email", validators=[DataRequired()])
    accepted_terms = BooleanField("I accept the terms and conditions", validators=[DataRequired()])
    submit = SubmitField("Submit Review")
