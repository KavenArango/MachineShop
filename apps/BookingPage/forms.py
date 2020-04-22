from flask_wtf import Form
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import InputRequired, length, Email, DataRequired
from wtforms.fields.html5 import TimeField, DateField, IntegerField


class BookingForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date_reserved = DateField('Date')
    start_time = TimeField('Start time')
    Machine_Name = StringField('Machine Name')


class BuildingSelect(Form):
    buildings = SelectField("Building", coerce=int, validators=[DataRequired()])
    rooms = SelectField("Room")
    submit = SubmitField('Edit Map')
