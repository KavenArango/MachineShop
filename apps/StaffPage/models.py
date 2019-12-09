from flask import Flask
from app import db
from apps.accounts import models
from apps.StudentPage import models
from apps.Machine import models
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'))


