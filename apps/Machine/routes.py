from flask import Blueprint
from flask import render_template, g

Machine_View = Blueprint('Machine_View', __name__)


@Machine_View.route('/machine')
def Machine():
    template = "Machine/MachineDes.html"
    return render_template(template)

