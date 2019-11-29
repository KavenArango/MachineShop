from flask import Blueprint
from flask import render_template,g

Student_view= Blueprint('Student_view', __name__)

@Student_view.route('/student')
def hello_world():
    return 'StudentPage'