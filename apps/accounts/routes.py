from flask import Blueprint, render_template, flash, redirect, url_for, app
from apps.accounts.forms import LoginForm, SignupForm
from app import db, bcrypt
from apps.accounts.models import Users
from flask_login import login_user, current_user, logout_user
from apps.StudentPage.models import majors, Student


login_view = Blueprint('login', __name__)


@login_view.route('/', methods=['get', 'post'])
def login_form():
    template = "accounts/login.html"
    title = "Login"
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('Main_View.home'))
        else:
            flash('Username or Password Incorrect')
    return render_template(template, title=title, form=form)


@login_view.route('/signup', methods=['get', 'post'])
def signup():
    form = SignupForm()
    form.major.choices = [(m.id, m.major_abbrev + " " + m.major_name) for m in majors.query.all()]
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data,
                     email=form.email.data, password=hashed_password)
        db.session.add(user)
        ID = Users.query.filter_by(username=form.username.data).first()
        for i in range(0, 5):
            student = Student(user_id=ID.id, major_id=form.major.data, machine_id=i, level_id=0)
            db.session.add(student)
        db.session.commit()
        flash('Your account has been created! You may now log in', 'success')
        return redirect(url_for('login.login_form'))
    return render_template("accounts/signup.html", title="Signup", form=form)


@login_view.route('/logout')
def logout():
    logout_user()
    flash('You have Logged Out')
    return redirect(url_for('login.login_form'))