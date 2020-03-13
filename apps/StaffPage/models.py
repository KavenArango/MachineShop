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

    def __repr__(self):
        return '<Request_Des %r>' % (self.description)

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'))
    requests_id = db.Column(db.Integer, db.ForeignKey('request__des.id'))

    user = db.relationship('Users', backref=db.backref('user_id', lazy='dynamic'))
    machine = db.relationship('machines', backref=db.backref('machine_id', lazy='dynamic'))
    level = db.relationship('Levels', backref=db.backref('level_id', lazy='dynamic'))
    request = db.relationship('Request_Des', backref=db.backref('requests_id', lazy='dynamic'))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('Users', backref=db.backref('author', lazy='dynamic'))

