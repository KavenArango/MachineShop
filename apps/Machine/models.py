from flask import Flask
from app import db

class machine_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_type = db.Column(db.String(100))
    def __repr__(self):
        return '<machine_type %r>' % (self.machine_type)
class machine_image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(100))


class machines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_name = db.Column(db.String(20))
    description = db.Column(db.String(180))
    machine_type_id = db.Column(db.Integer, db.ForeignKey('machine_type.id'))
    machine_type = db.relationship('machine_type', backref=db.backref('machine_type_id', lazy='dynamic'))
    def __repr__(self):
        return '<machines %r>' % (self.machine_name)
class building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_name = db.Column(db.String(100))

class room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_num = db.Column(db.Integer)
    room_outline = db.Column(db.String(100))
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'))

class machine_join(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))
    x_pos = db.Column(db.Integer)
    y_pos = db.Column(db.Integer)

class machine_shop_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    machine_join_id = db.Column(db.Integer, db.ForeignKey('machine_join.id'))