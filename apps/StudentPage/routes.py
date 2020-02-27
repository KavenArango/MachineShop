from flask import Blueprint, redirect, url_for, flash
from flask import render_template, g
from .forms import RequestForm, RequestExamForm, Student_info
from .models import Levels
from apps.StaffPage.models import Request, Request_Des
from apps.Machine.models import machines
from apps.accounts.models import Users
from apps.StudentPage.models import Student, majors
from flask_login import current_user, login_required
from app import db
from apps.StaffPage.models import Post
Student_view = Blueprint('Student_view', __name__)


@Student_view.route('/studentprofile')
@login_required
def profile():
    template = "StudentPage/StudentProfile.html"
    title = "Profile"
    post = Student.query.filter(Student.user_id == current_user.id).filter(Student.machine_id ).join(
        Users, Users.id == Student.user_id
    ).join(
        machines, machines.id == Student.machine_id
    ).join(
        majors, majors.id == Student.major_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        Student.id.label("id"),
        machines.machine_name.label("machine_name"),
        Levels.description.label("description"),
        Users.id.label("User_id")
    ).first()


    detail = Student.query.filter(Student.user_id == post.User_id).join(
        machines, machines.id == Student.machine_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        machines.machine_name.label("machine_name"),
        Levels.description.label("description")
    ).all()

    return render_template(template, title=title, detail=detail)
@Student_view.route('/studentProfileInfo/<user_id>' , methods=['get', 'post'])
@login_required
def studentProfileInfo(user_id):
    template = "StudentPage/StudentInfoEdit.html"
    title = "Student Detail"
    form = Student_info()
    post = Users.query.filter(Users.id == user_id).join(
        Student, Student.user_id == Users.id
    ).join(
        majors, majors.id == Student.major_id
    ).with_entities(
        Student.id.label("id"),
        Users.first_name.label("first_name"),
        Users.last_name.label("last_name"),
        Users.email.label("email"),
        majors.major_name.label("major_name"),


    ).first()
    form.first_name.data = post.first_name
    form.last_name.data = post.last_name
    form.email.data = post.email
    form.major.data = post.major_name
    user = Users.query.filter_by(email=form.email.data).first()
    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        db.session.commit()
        flash('Your Info Has Been Updated', 'success')

        #You Are HERE STEVEN
        return redirect(url_for('Student_view.profile'))
    return render_template(template, title=title, form=form)

@Student_view.route('/request', methods=['get', 'post'])
@login_required
def requests():
    form = RequestForm()
    form1 = RequestExamForm()

    if current_user.passed_exam >= 0:
        form.request.choices = [(Requests.id, Requests.description) for Requests in Request_Des.query.filter_by(id=2)]
        form.level.choices = [(Level.level, Level.description) for Level in Levels.query.all()]
        form.machine.choices = [(Machine.id, Machine.machine_name) for Machine in machines.query.all()]
        if form.validate_on_submit():
            request = Request(user_id=current_user.id, machine_id=form.machine.data,
                              level_id=form.level.data, requests_id=form.request.data)
            db.session.add(request)
            db.session.commit()
            return redirect(url_for('Main_View.home'))
        return render_template("StudentPage/request.html", title="Request Form", form=form)
    else:
        form1.requests.choices = [(Requests.id, Requests.description) for Requests in Request_Des.query.filter_by(id=1)]
        if form1.validate_on_submit():
            request = Request(user_id=current_user.id, machine_id=0, level_id=-1, requests_id=form1.requests.data)
            db.session.add(request)
            db.session.commit()
            return redirect(url_for('Main_View.home'))
        return render_template("StudentPage/examRequest.html", title="Request Form", form1=form1)

@Student_view.route('/announcement')
@login_required
def post():
    posts = Post.query.all()
    return render_template("StudentPage/Post.html", title="Announcement", posts=posts)