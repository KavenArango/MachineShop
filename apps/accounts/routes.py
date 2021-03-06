from flask import Blueprint, render_template, flash, redirect, url_for, app, Markup
from apps.accounts.forms import LoginForm, SignupForm, resetForm, forgetForm
from app import db, bcrypt, login_manager, client, url
from apps.accounts.models import Users
from flask_login import login_user, current_user, logout_user, login_required
from apps.StudentPage.models import majors, Student
from app import mail
from flask_mail import Message
from itsdangerous import SignatureExpired
from apps.StudentPage.models import Student, majors, Levels, Notification
from datetime import datetime


login_view = Blueprint('login', __name__)


@login_view.route('/', methods=['get', 'post'])
def login_form():
    template = "accounts/login.html"
    title = "Login"
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data) and user.user_type == 2:
            login_user(user)
            return redirect(url_for('admin.index'))
        elif user and bcrypt.check_password_hash(user.password, form.password.data) and user.user_type == 3:
            login_user(user)
            return redirect(url_for('Tool_View.CheckIn'))
        elif user and bcrypt.check_password_hash(user.password, form.password.data):
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
                     email=form.email.data, password=hashed_password, user_type=0, passed_exam=1, email_ver=0)
        db.session.add(user)
        ID = Users.query.filter_by(username=form.username.data).first()
        for i in range(1, 6):
            student = Student(user_id=ID.id, major_id=form.major.data, machine_id=i, level_id=1)
            db.session.add(student)
        db.session.commit()
        notification = Notification(user_id=user.id, description="Welcome to the Machine Shop", delete_bool=1,
                                    date_receive=datetime.now())
        db.session.add(notification)
        db.session.commit()
        token = url.dumps(form.email.data, salt='email-confirm')

        msg = Message(subject='Welcome to the Machine Shop', recipients=[form.email.data])
        link = url_for('login.confirm_email', token=token, _external=True)
        msg.html = 'Please verify your email <a href="{}">Click Me </a>'.format(link)
        mail.send(msg)
        flash('Your account has been created! You may now log in', 'success')
        return redirect(url_for('login.login_form'))

    return render_template("accounts/signup.html", title="Signup", form=form)


@login_view.route('/confirm_email/<token>')
def confirm_email(token):
    try:

        email = url.loads(token, salt='email-confirm', max_age=900)

    except SignatureExpired:
        flash(Markup('The Token is Expired! <a href="/resend" class="alert-link">Resend Email Verification</a>' ))
        return redirect(url_for('login.login_form'))
    except:
        flash(Markup('The Token doesnt Exisit!'))
        return redirect(url_for('login.login_form'))
    user = Users.query.filter_by(email=email).first()
    user.email_ver = 1
    db.session.commit()
    flash('Email has be verified! You may log in')
    return redirect(url_for('login.login_form'))

@login_view.route('/forgotPassword', methods=['get', 'post'])
def forgotPassword():
    form = forgetForm()
    if form.validate_on_submit():
        token = url.dumps(form.email.data, salt='pass-confirm')

        msg = Message(subject='Forgot Password', recipients=[form.email.data])
        link = url_for('login.reset_pass',token=token, _external=True)
        msg.html = 'Please Click on the link to reset password! <a href="{}">Click Me </a>'.format(link)
        mail.send(msg)
        flash('An Email Has Been Sent To Reset Your Password', 'success')
        return redirect(url_for('login.login_form'))



    return render_template("accounts/forgot.html", form=form)


@login_view.route('/resetPass/<token>')
def reset_pass(token):
    try:

       email = url.loads(token, salt='pass-confirm', max_age=900)

    except SignatureExpired:
        flash(Markup('The Token is Expired! <a href="/resend" class="alert-link">Resend Email Verification</a>' ))
        return redirect(url_for('login.login_form'))
    except:
        flash(Markup('The Token doesnt Exisit!'))
        return redirect(url_for('login.login_form'))
    return redirect(url_for('login.reset_input', token=token))

@login_view.route('/resetInput/<token>', methods=['get', 'post'])
def reset_input(token):
    template = 'accounts/reset_pass.html'
    email = url.loads(token, salt='pass-confirm', max_age=900)
    user = Users.query.filter_by(email=email).first()
    form = resetForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Password Has been Reset ! You may log in')
        return redirect(url_for('login.login_form'))
    return render_template(template, form=form)

@login_view.route('/resend')
@login_required
def resend():
    token = url.dumps(current_user.email, salt='email-confirm')

    msg = Message(subject='Email Conformation', recipients=[current_user.email])
    link = url_for('login.confirm_email', token=token, _external=True)
    msg.html = 'Please verify your email <a href="{}">Click Me </a>'.format(link)
    mail.send(msg)
    #logout_user()
    flash('Email Verification sent!')
    return redirect(url_for('Main_View.home'))

@login_view.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have Logged Out')
    return redirect(url_for('login.login_form'))

@login_view.route('/send', methods=['get', 'post'])
def send():
    client.send_message({'from': '15739191005', 'to': '13055100402', 'text': 'A message has been sent from MachineShop'})
    flash('Sent')
    return redirect(url_for('login.login_form'))


