from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import InputRequired, length, Email, DataRequired
from wtforms.fields.html5 import TimeField, DateField, IntegerField


class BookingForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date_reserved = DateField('Date')
    start_time = TimeField('Start time')
    Machine_Name = StringField('Machine Name')


class BuildingSelect(FlaskForm):
    buildings = SelectField("", coerce=int, validators=[DataRequired()])
    rooms = SelectField("")
    submit = SubmitField('Select Room')
