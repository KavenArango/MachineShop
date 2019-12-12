from flask import Flask
from app import db
from apps.accounts import models
from apps.StudentPage import models
from apps.Machine import models
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Request_Des(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150))

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'))

class Booking(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        group_id = db.Column(db.Integer, db.ForeignKey('group_join.id'))
        machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))
        booking_For_Date = db.Column(db.DATE)
        Start_Time = db.Column(db.DATETIME)
