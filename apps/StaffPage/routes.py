from flask import Blueprint
from flask import render_template,g

Staff_View = Blueprint('Staff_View', __name__)

@Staff_View.route('/staff')
def staff():
    template = "StaffPage/staff.html"
    title = "staff"
    return render_template(template, title=title)
