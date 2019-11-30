from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, length, Email, DataRequired,EqualTo,ValidationError
from apps.accounts.models import Users

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Email(message='Please enter a valid username')])
    password = PasswordField("password", validators=[DataRequired(), length(min=5, max=10)])


class SignupForm(FlaskForm):
    first_name = StringField("first name", validators=[DataRequired()])
    last_name = StringField("last name", validators=[DataRequired()])
    username = StringField("username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

