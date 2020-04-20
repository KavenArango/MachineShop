from flask import Blueprint, redirect, url_for, flash, Markup
from flask import render_template, g, request, app
import secrets
import os
from PIL import Image
from apps.StudentPage.forms import RequestForm, RequestExamForm, Profile
from apps.StudentPage.models import Levels
from apps.StaffPage.models import Request, Request_Des
from apps.Machine import models
from apps.accounts.models import Users
from apps.StudentPage.models import Student, majors, Notification
from flask_login import current_user, login_required
from app import db, app
from apps.StaffPage.models import Post
from datetime import datetime

Student_view = Blueprint('Student_view', __name__)



@Student_view.route('/studentprofile')
@login_required
def profile():
    template = "StudentPage/StudentProfile.html"
    title = "Profile"
    post = Student.query.filter(Student.user_id == current_user.id).join(
        Users, Users.id == Student.user_id
    ).join(
        models.machines, models.machines.id == Student.machine_id
    ).join(
        majors, majors.id == Student.major_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        Student.id.label("id"),
        models.machines.machine_name.label("machine_name"),
        Levels.description.label("description"),
        Users.id.label("User_id")
    ).first()

    detail = Student.query.filter(Student.user_id == post.User_id).join(
        models.machines, models.machines.id == Student.machine_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        models.machines.machine_name.label("machine_name"),
        Levels.description.label("description")
    ).all()

    return render_template(template, title=title, detail=detail)





@Student_view.route('/request', methods=['get', 'post'])
@login_required
def requests():
    form = RequestForm()
    form1 = RequestExamForm()
    form2 = Profile()
    post = Student.query.filter(Student.user_id == current_user.id).join(
        Users, Users.id == Student.user_id
    ).join(
        models.machines, models.machines.id == Student.machine_id
    ).join(
        majors, majors.id == Student.major_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        Student.id.label("id"),
        models.machines.machine_name.label("machine_name"),
        Levels.description.label("description"),
        Users.id.label("User_id")
    ).first()

    detail = Student.query.filter(Student.user_id == post.User_id).join(
        models.machines, models.machines.id == Student.machine_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        models.machines.machine_name.label("machine_name"),
        Levels.description.label("description")
    ).all()

    if form2.validate_on_submit():
        if form2.picture.data:
            picture_file = save_picture(form2.picture.data)
            current_user.profile_pic = picture_file
            db.session.commit()
            flash('Your Profile Picture Has Been Updated')
            return redirect(url_for('Student_view.requests'))
    if (current_user.email_ver < 1):
        flash(Markup(
            'You Must Verify Email To Access <a href="/resend" class="alert-link">Resend Email Verification?</a>', ))
        return redirect(url_for('Main_View.home'))
    if current_user.passed_exam > 1:
        form.request.choices = [(Requests.id, Requests.description) for Requests in Request_Des.query.filter_by(id=2)]
        form.level.choices = [(Level.level, Level.description) for Level in Levels.query.all()]
        form.machine.choices = [(Machine.id, Machine.machine_name) for Machine in models.machines.query.all()]
        if form.validate_on_submit():
            request = Request(user_id=current_user.id, machine_id=form.machine.data,
                              level_id=form.level.data, requests_id=form.request.data)
            db.session.add(request)
            db.session.commit()
            notification = Notification(user_id=current_user.id, description="You have Succefully submmited a you lab"
                                                                             "safety request!",
                                        delete_bool=0, date_receive=datetime.now())
            db.session.add(notification)
            db.session.commit()
            return redirect(url_for('Main_View.home'))
        image = url_for('static', filename="media/"+ current_user.profile_pic)
        return render_template("StudentPage/request.html", title="Request Form", form=form, form2=form2, detail=detail, image=image)
    else:

        form1.requests.choices = [(Requests.id, Requests.description) for Requests in Request_Des.query.filter_by(id=1)]
        if form1.validate_on_submit():
            request = Request(user_id=current_user.id, machine_id=1, level_id=1, requests_id=form1.requests.data)
            db.session.add(request)
            db.session.commit()
            notification = Notification(user_id=current_user.id, description="You have Succefully submmited a request!",
                                        delete_bool=0, date_receive=datetime.now())
            db.session.add(notification)
            db.session.commit()
            return redirect(url_for('Main_View.home'))
        image = url_for('static', filename="media/" + current_user.profile_pic)
    return render_template("StudentPage/examRequest.html", title="Request Form", form1=form1, form2=form2, detail=detail, image=image)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.config['UPLOAD_FOLDER'], picture_fn)

    output_size = (300,300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(os.path.join(app.config['UPLOAD_FOLDER'], picture_fn))
    print(picture_fn)
    return picture_fn

@Student_view.route('/announcement')
@login_required
def post():
    posts = Post.query.filter(Post.author == Users.id).join(
        Users, Users.id == Post.author
    ).with_entities(
        Post.id.label("id"),
        Users.first_name.label("first_name"),
        Users.last_name.label("last_name"),
        Post.content.label("content"),
        Post.title.label("title"),
        Post.date_posted.label("date_posted")
    ).all()
    return render_template("StudentPage/Post.html", title="Announcement", posts=posts)