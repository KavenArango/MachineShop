from flask import Flask
from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(20),nullable=False)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    user_type = db.Column(db.Integer,)



