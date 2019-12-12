from flask import Blueprint, redirect, url_for, request, flash
from flask import render_template,g
from app import db
from apps.accounts.models import Users
from apps.StudentPage.models import Student, majors, Levels
from apps.StaffPage.forms import Staff_Student, Staff_Request, Staff_AddMachine
from apps.Machine.models import machines
from pymysql import NULL
from sqlalchemy import and_
from .models import Request, Request_Des
from flask_paginate import Pagination, get_page_parameter

Staff_View = Blueprint('Staff_View', __name__)


@Staff_View.route('/studentsearch')
def student_search():
    template = "StaffPage/StudentSearch.html"
    title = "Student Search"
    form = Staff_Student()
    students = Student.query.distinct(Users.email).group_by(Users.email).filter(Student.user_id == Users.id).join(
        Users, Users.id == Student.user_id
    ).join(
        machines, machines.id == Student.machine_id
    ).join(
        majors, majors.id == Student.major_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        Student.id.label("id"),
        Users.first_name.label("first_name"),
        Users.last_name.label("last_name"),
        Users.email.label("email"),
        majors.major_name.label("major_name"),
        machines.machine_name.label("machine_name"),
        Levels.description.label("level")
    ).all()
    return render_template(template, title=title, students=students, form=form)

@Staff_View.route('/studentdetail/<student_id>')
def student_detail(student_id):
    template = "StaffPage/studentdetail.html"
    title = "Student Detail"
    form = Staff_Student()
    post = Student.query.filter(Student.id == student_id).join(
        Users, Users.id == Student.user_id
    ).join(
        machines, machines.id == Student.machine_id
    ).join(
        majors, majors.id == Student.major_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        Student.id.label("id"),
        Users.first_name.label("first_name"),
        Users.last_name.label("last_name"),
        Users.email.label("email"),
        majors.major_name.label("major_name"),
        machines.machine_name.label("machine_name"),
        Levels.description.label("description"),
        Users.id.label("User_id")
    ).first()
    form.first_name.data = post.first_name
    form.last_name.data = post.last_name
    form.email.data = post.email
    form.major.data = post.major_name

    detail = Student.query.filter(Student.user_id == post.User_id).filter(machines.id != 0).join(
        machines, machines.id == Student.machine_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        machines.machine_name.label("machine_name"),
        Levels.description.label("description")
    ).all()

    return render_template(template, title=title, form=form, detail=detail)

@Staff_View.route('/requestsearch')
def request_search():
    template = "StaffPage/Request.html"
    title = "Request Search"
    form = Staff_Request()
    requests = Request.query.filter(Request.user_id == Users.id).join(
        Users, Users.id == Request.user_id
    ).join(
        machines, machines.id == Request.machine_id
    ).join(
        Levels, Levels.id == Request.level_id
    ).join(
        Request_Des, Request_Des.id == Request.requests_id
    ).with_entities(
        Request.id.label("id"),
        Users.first_name.label("first_name"),
        Users.last_name.label("last_name"),
        machines.machine_name.label("machine_name"),
        Levels.description.label("level"),
        Request_Des.description.label('Request')
    ).all()
    return render_template(template, title=title, requests=requests, form=form)


@Staff_View.route('/requestsearch/<request_id>', methods=['get', 'post'])
def request_detail(request_id):
    template = "StaffPage/requestdetails.html"
    title = "Request Detail"
    form = Staff_Request()
    post = Request.query.filter(Request.id == request_id).join(
        Users, Users.id == Request.user_id
    ).join(
        machines, machines.id == Request.machine_id
    ).join(
        Levels, Levels.id == Request.level_id
    ).join(
        Request_Des, Request_Des.id == Request.requests_id
    ).with_entities(
        Request.id.label("id"),
        Users.first_name.label("first_name"),
        Users.last_name.label("last_name"),
        machines.machine_name.label("machine_name"),
        Levels.description.label("description"),
        Request_Des.description.label('Request')
    ).first()
    form.first_name.data = post.first_name
    form.last_name.data = post.last_name
    form.machine.data = post.machine_name
    form.level.data = post.description
    form.des.data = post.Request


    user = Users.query.filter_by(first_name=post.first_name).first()
    levelUp = Student.query.filter_by(user_id=user.id).all()
    if form.validate_on_submit():

        if user.passed_exam < 1:
            user.passed_exam = 1
            for levelups in levelUp:
                levelups.level_id = levelups.level_id + 1
            db.session.commit()
            Request.query.filter_by(id=post.id).delete()
            return redirect(url_for('Staff_View.request_search'))
        else:
            machine = machines.query.filter_by(machine_name=post.machine_name).first()
            level = Levels.query.filter_by(description=post.description).first()
            student = Student.query.filter_by(user_id=user.id, machine_id=machine.id).first()
            if student.level_id > level.id:
                Request.query.filter_by(id=post.id).delete()
                return redirect(url_for('Staff_View.request_search'))
            elif student.level_id != level.id:
                if student.level_id + 2 == level.id:
                    Request.query.filter_by(id=post.id).delete()
                    return redirect(url_for('Staff_View.request_search'))
                elif student.level_id + 3 == level.id:
                    Request.query.filter_by(id=post.id).delete()
                    return redirect(url_for('Staff_View.request_search'))
                elif student.level_id + 4 == level.id:
                    Request.query.filter_by(id=post.id).delete()
                    return redirect(url_for('Staff_View.request_search'))
                else:
                    student.level_id = level.id
                    db.session.commit()
                    Request.query.filter_by(id=post.id).delete()
                    return redirect(url_for('Staff_View.request_search'))
            else:
                Request.query.filter_by(id=post.id).delete()
                return redirect(url_for('Staff_View.request_search'))

    return render_template(template, title=title, form=form)




