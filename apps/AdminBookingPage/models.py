from flask import Flask
from app import db
from apps.BookingPage import models
from apps.accounts import models
from apps.StudentPage import models
from apps.Machine import models
from datetime import datetime


class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_name = db.Column(db.String)
