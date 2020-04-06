from flask import Blueprint, flash
from flask import render_template,g
from flask_login import current_user, login_required
from flask import Markup
from apps.StudentPage.models import Notification
Main_View = Blueprint('Main_View', __name__)

@Main_View.route('/homepage')
@login_required
def home():
    template = "Home Page/Homepage.html"
    notifications = Notification.query.filter(Notification.user_id == current_user.id).all()
    if current_user.email_ver == 0:
        flash(Markup('Email not verified!  <a href="/resend" class="alert-link">Resend?</a>'))



    return render_template(template, notifications=notifications)


