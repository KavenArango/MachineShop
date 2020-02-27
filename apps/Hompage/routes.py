from flask import Blueprint
from flask import render_template,g
from flask_login import current_user, login_required

Main_View = Blueprint('Main_View', __name__)

@Main_View.route('/homepage')
@login_required
def home():
    template = "Home Page/Homepage.html"
    return render_template(template)

