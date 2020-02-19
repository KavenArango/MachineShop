from flask import Flask
from app import db
from apps.accounts import models
from apps.StudentPage import models
from apps.Machine import models
from datetime import datetime


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #group_id = db.Column(db.Integer, db.ForeignKey('group_join.id'))
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))
    booking_For_Date = db.Column(db.DATE)
    Booked_date = db.Column(db.DATE)
    Start_Time = db.Column(db.Integer)
    Key = db.Column(db.Integer)


# class GroupJoin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
