from flask import Flask
from datetime import datetime
from app import db
from apps.accounts import models
from apps.StudentPage import models
from apps.Machine import models
from datetime import datetime


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
    requests_id = db.Column(db.Integer, db.ForeignKey('request__des.id'))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String, db.ForeignKey('users.first_name'), nullable=False)

