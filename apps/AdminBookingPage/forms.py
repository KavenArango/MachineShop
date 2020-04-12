from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import InputRequired, length, Email, DataRequired, EqualTo, ValidationError, NumberRange
from flask_wtf.file import FileAllowed, FileField
from apps.Machine.models import room


class RoomForm(FlaskForm):
    RoomNum = IntegerField("", validators=[DataRequired("Input a number"),NumberRange(min=100, max=999, message="Input a number from 100 - 999")])
    Building = SelectField("", coerce=int, validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Create Room")

    def validate_Room(self, RoomNum, Building):
        room_num = room.query.filter_by(room_num=RoomNum.data).first()
        if room_num:
            raise ValidationError('That Room number is taken.')

class BuildingSelect(FlaskForm):
    buildings = SelectField("Building", coerce=int, validators=[DataRequired()])
    rooms = SelectField("Room" )
    submit = SubmitField('Submit Form')
