from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, length, Email, DataRequired, EqualTo, ValidationError


class RequestForm(FlaskForm):
    request = SelectField("Request", coerce=int, validators=[DataRequired()])
    machine = SelectField("Machine", coerce=int, validators=[DataRequired()])
    level = SelectField("Level", coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit Form')


class RequestExamForm(FlaskForm):
    requests = SelectField("Request", coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit Form')
