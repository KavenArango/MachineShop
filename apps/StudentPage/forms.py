from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from flask_wtf.file import FileAllowed, FileField
from wtforms.validators import InputRequired, length, Email, DataRequired, EqualTo, ValidationError


class RequestForm(FlaskForm):
    request = SelectField("Request", coerce=int, validators=[DataRequired()])
    machine = SelectField("Machine", coerce=int, validators=[DataRequired()])
    level = SelectField("Level", coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit Form')



class RequestExamForm(FlaskForm):
    requests = SelectField("Passed Exam",coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit Form')

class Profile(FlaskForm):
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update Photo')