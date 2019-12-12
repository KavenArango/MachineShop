from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, length, Email, DataRequired,EqualTo,ValidationError
from apps.accounts.models import Users

class Staff_Student(Form):
    first_name = StringField('first name')
    last_name = StringField('last name')
    email = StringField('Email')
    major = StringField('Major')

class Staff_Request(Form):
    first_name = StringField('first name')
    last_name = StringField('last name')
    machine = StringField('Machine')
    level = StringField('Level')
    des = StringField('Request')
    accept = SubmitField('Accept')
    decline = SubmitField('Reject')