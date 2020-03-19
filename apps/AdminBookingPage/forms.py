from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, length, Email, DataRequired, EqualTo, ValidationError
from apps.Machine import models


class Roomform(FlaskForm):
    RoomNum = StringField("", validators=[DataRequired()])
    RoomName = StringField("", validators=[DataRequired()])
    Building = SelectField("", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Create Room")

