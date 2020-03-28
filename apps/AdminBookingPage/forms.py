from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import InputRequired, length, Email, DataRequired, EqualTo, ValidationError, NumberRange
from apps.Machine import models


class Roomform(FlaskForm):
    RoomNum = IntegerField("", validators=[DataRequired("Input a number"),
                                           NumberRange(min=100, max=999, message="Input a number from 100 - 999")])
    Building = SelectField("", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Create Room")