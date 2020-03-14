from flask import Blueprint, redirect, url_for, flash, abort, request
from flask import render_template, g
from app import db
from apps.accounts.models import Users
from apps.StudentPage.models import Student, majors, Levels
from apps.StaffPage.forms import Staff_Student, Staff_Request, PostForm
from apps.Machine.models import machines
from .models import Request, Request_Des, Post
from flask_login import current_user, login_required

Staff_View = Blueprint('Staff_View', __name__)


@Staff_View.route('/studentsearch')
@login_required
def student_search():
    template = "StaffPage/StudentSearch.html"
    title = "Student Search"
    form = Staff_Student()
    students = Student.query.distinct(Users.email).group_by(Users.email).filter(Student.user_id == Users.id).join(
        Users, Users.id == Student.user_id
    ).join(
        majors, majors.id == Student.major_id
    ).with_entities(
        Users.first_name.label("first_name"),
        Users.last_name.label("last_name"),
        Users.email.label("email"),
        majors.major_name.label("major_name"),
    ).all()
    return render_template(template, title=title, students=students, form=form)


@Staff_View.route('/studentdetail/<student_id>')
@login_required
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
@login_required
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

@Staff_View.route("/requestsearch/int::<requestDelete_id>/delete", methods=[ 'post'])
@login_required
def delete_request(requestDelete_id):
    Request.query.filter_by(id=requestDelete_id).delete()
    db.session.commit()
    flash('You have Rejected the request', 'success')
    return redirect(url_for('Staff_View.request_search'))

@Staff_View.route('/requestsearch/<request_id>', methods=['get', 'post'])
@login_required
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

        if user.passed_exam == -1:
            user.passed_exam = 0
            for levelups in levelUp:
                levelups.level_id = levelups.level_id + 1
            db.session.commit()
            Request.query.filter_by(id=post.id).delete()
            flash('test1')
            return redirect(url_for('Staff_View.request_search'))
        else:
            machine = machines.query.filter_by(machine_name=post.machine_name).first()
            level = Levels.query.filter_by(description=post.description).first()
            student = Student.query.filter_by(user_id=user.id, machine_id=machine.id).first()
            if student.level_id > level.id:
                Request.query.filter_by(id=post.id).delete()
                flash('test2')
                return redirect(url_for('Staff_View.request_search'))
            elif student.level_id != level.id:
                if student.level_id + 2 == level.id:
                    Request.query.filter_by(id=post.id).delete()
                    flash('test3')
                    return redirect(url_for('Staff_View.request_search'))
                elif student.level_id + 3 == level.id:
                    Request.query.filter_by(id=post.id).delete()
                    flash('test4')
                    return redirect(url_for('Staff_View.request_search'))
                elif student.level_id + 4 == level.id:
                    Request.query.filter_by(id=post.id).delete()
                    flash('test5')
                    return redirect(url_for('Staff_View.request_search'))
                else:
                    student.level_id = level.id
                    db.session.commit()
                    Request.query.filter_by(id=post.id).delete()
                    flash('test6')
                    return redirect(url_for('Staff_View.request_search'))
            else:
                Request.query.filter_by(id=post.id).delete()
                flash('test7')
                return redirect(url_for('Staff_View.request_search'))

    return render_template(template, title=title, form=form)



@Staff_View.route("/post", methods=['GET', 'POST'])
@login_required
def newPost():
    template = "StaffPage/createPost.html"
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user.first_name)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('Student_view.post'))
    return render_template(template, title='New Post', form=form, legend='New Post')


@Staff_View.route("/post/<int:post_id>")
@login_required
def post(post_id):
    post = Post.query.get(post_id)
    return render_template("StaffPage/PostDetail.html", title=post.title, post=post)


@Staff_View.route("/post/<int:post_id>/update", methods=['get', 'post'])
@login_required
def update_post(post_id):
    post = Post.query.get(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('Staff_View.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('StaffPage/createPost.html', title='Update Post',
                           form=form, legend='Update Post')

@Staff_View.route("/post/<int:post_id>/delete", methods=['post'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user.first_name:
        redirect('Student.view.post')
        flash('You can not delete this post')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Your post has been deleted!', 'success')
    return redirect(url_for('Student_view.post'))
