from flask import Flask
from app import db
from apps.accounts import models
from apps.Machine import models


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('group_join.id'))
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))
    booking_For_Date = db.Column(db.DATE)
    Start_Time = db.Column(db.DATETIME)


class GroupJoin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
