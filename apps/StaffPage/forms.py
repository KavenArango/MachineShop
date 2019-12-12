from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, length, Email, DataRequired,EqualTo,ValidationError
from apps.accounts.models import Users
from wtforms_components import read_only

class Staff_Student(Form):
    first_name = StringField('first name')
    last_name = StringField('last name')
    email = StringField('Email')
    major = StringField('Major')

    def __init__(self, *args, **kwargs):
        super(Staff_Student, self).__init__(*args, **kwargs)
        read_only(self.first_name)
        read_only(self.last_name)
        read_only(self.email)
        read_only(self.major)

class Staff_Request(Form):
    first_name = StringField('first name')
    last_name = StringField('last name')
    machine = StringField('Machine')
    level = StringField('Level')
    des = StringField('Request')
    accept = SubmitField('Accept')
    decline = SubmitField('Reject')

    def __init__(self, *args, **kwargs):
        super(Staff_Request, self).__init__(*args, **kwargs)
        read_only(self.first_name)
        read_only(self.last_name)
        read_only(self.machine)
        read_only(self.level)
        read_only(self.des)


class Staff_AddMachine(Form):
    machine_name = StringField('Machine Name')
    description = StringField('Description')
    submit = SubmitField('Add Machine')