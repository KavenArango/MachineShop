from flask import Blueprint
from flask import render_template, g
from flask_login import login_required

Machine_View = Blueprint('Machine_View', __name__)


@Machine_View.route('/machine')
@login_required
def Machine():
    template = "Machine/MachineDes.html"
    return render_template(template)

