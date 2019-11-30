from flask import Blueprint, render_template, flash, redirect, url_for,app
from apps.accounts.forms import LoginForm, SignupForm
from app import db,bcrypt
from apps.accounts.models import Users





login_view = Blueprint('login', __name__)


@login_view.route('/', methods=['Get', 'POST'])
def login_form():
    template = "accounts/login.html"
    title = "Login"
    form = LoginForm()
    return render_template(template, title=title, form=form)



@login_view.route('/signup', methods=['get', 'post'])
def signup():
    form = SignupForm()
    if form.is_submitted():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data,
                     email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You may now log in', 'success')
        return redirect(url_for('login.login_form'))



    return render_template("accounts/signup.html", title="Signup", form=form)
