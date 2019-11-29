from flask import Flask
from app import db
from apps.accounts import models
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


