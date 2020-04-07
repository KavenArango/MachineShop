from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, length, Email, DataRequired, EqualTo, ValidationError
from apps.accounts.models import Users


class LoginForm(FlaskForm):
    username = StringField("", validators=[DataRequired()])
    password = PasswordField("", validators=[DataRequired()])
    submit = SubmitField("Login")


class SignupForm(FlaskForm):
    first_name = StringField("", validators=[DataRequired()])
    last_name = StringField("", validators=[DataRequired()])
    username = StringField("", validators=[DataRequired()])
    major = SelectField("", coerce=int, validators=[DataRequired()])
    email = StringField("", validators=[DataRequired(), Email()])
    password = PasswordField("", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class resetForm(FlaskForm):
    password = PasswordField("", validators=[DataRequired()])
    submit = SubmitField("Change")

class forgetForm(FlaskForm):
    email = StringField("", validators=[DataRequired(), Email()])
    submit = SubmitField("Reset")
