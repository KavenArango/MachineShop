from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import InputRequired, length, Email
from wtforms.fields.html5 import TimeField, DateField


class BookingForm(Form):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    date_reserved = DateField('Date')
    start_time = TimeField('Start time')
    end_time = TimeField('End time')
