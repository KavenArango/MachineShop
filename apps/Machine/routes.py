from flask import Blueprint
from flask import render_template, g
from flask_login import login_required, current_user
from apps.StudentPage.models import Notification

Machine_View = Blueprint('Machine_View', __name__)


@Machine_View.route('/machine')
@login_required
def Machine():
    template = "Machine/MachineDes.html"
    notifications = Notification.query.filter(Notification.user_id == current_user.id).all()
    return render_template(template, notifications=notifications)

