from flask import Flask
from app import db, login_manager



class tool_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80),nullable=False)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    tool = db.Column(db.string(100), nullable=False)