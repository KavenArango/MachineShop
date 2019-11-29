from flask import Flask
from app import db
from apps.accounts import models
from apps.Machine import models

class Levels(db.Model):
    __tablename__ = "levels"
    id = db.Column(db.Integer,primary_key=True)
    level = db.Column(db.Integer)
    description = db.Column(db.String(150))

    def __init__(self,level, descriptions):
        self.level = level
        self.description = descriptions
    def __repr__(self):
        return  '<{}>'.format(self.level)

class Student_level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'))

    def __init__(self,student_id,machine_id,level_id):
            self.student_id = student_id
            self.machine_id = machine_id
            self.level_id = level_id



class majors(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    major_name = db.Column(db.String(100))
    major_abbrev = db.Column(db.String(10))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    major_id = db.Column(db.Integer, db.ForeignKey('majors.id'))
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'))
