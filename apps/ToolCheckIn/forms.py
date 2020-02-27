from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, length, Email, DataRequired,EqualTo,ValidationError
from wtforms_components import read_only

from apps.accounts.models import Users

class CheckInForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    tool = StringField("Tool Name", validators=[DataRequired()])
    submit = SubmitField("Check In")

class CheckIn_Users(FlaskForm):
    first_name = StringField('first name')
    last_name = StringField('last name')
    email = StringField('Email')
    tool = StringField("Tool Name")
    submit = SubmitField("Check Out")

class Checkout(FlaskForm):
    submit = SubmitField("Check Out")