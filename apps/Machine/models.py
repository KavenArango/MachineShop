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

class room_image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(100))
    def __repr__(self):
        return '<room_image %r>' % (self.image)

class machines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_name = db.Column(db.String(20))
    description = db.Column(db.String(500))
    machine_type_id = db.Column(db.Integer, db.ForeignKey('machine_type.id'))
    machine_type = db.relationship('machine_type', backref=db.backref('machine_type_id', lazy='dynamic'))

    def __repr__(self):
        return '<machines %r>' % (self.machine_name)


class building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_name = db.Column(db.String(100))
    def __repr__(self):
        return '<building %r>' % (self.building_name)


class room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_num = db.Column(db.Integer)
    room_image = db.Column(db.Integer, db.ForeignKey('room_image.id'))
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'))
    building = db.relationship('building', backref=db.backref('building_id', lazy='dynamic'))
    room_images = db.relationship('room_image', backref=db.backref('room_image', lazy='dynamic'))


    building = db.relationship('building', backref=db.backref('building_id', lazy='dynamic'))
    room_images = db.relationship('room_image', backref=db.backref('room_image', lazy='dynamic'))
class machine_join(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))
    x_pos = db.Column(db.Integer)
    y_pos = db.Column(db.Integer)


class machine_shop_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    machine_join_id = db.Column(db.Integer, db.ForeignKey('machine_join.id'))


class tool_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    tool = db.Column(db.String(100), nullable=False)
    check_in_date = db.Column(db.Date)
    check_out_date = db.Column(db.Date)
    checked = db.Column(db.Integer)
