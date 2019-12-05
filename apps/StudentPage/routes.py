from flask import Blueprint
from flask import render_template,g
from .forms import RequestForm
from .models import Levels
from apps.Machine.models import machines
Student_view= Blueprint('Student_view', __name__)

@Student_view.route('/request')
def hello_world():
    form = RequestForm()
    form.level.choices = [(str(Level.id), str(Level.level) + " " + Level.description) for Level in Levels.query.all()]
    form.machine.choices = [(Machine.id, Machine.machine_name) for Machine in machines.query.all()]

    return render_template("StudentPage/request.html", title="Request Form", form=form)