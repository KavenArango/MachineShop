from flask import Flask
from app import db


class machines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_name = db.Column(db.String(20))
    description = db.Column(db.String(180))

