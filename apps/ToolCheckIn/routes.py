from flask import Blueprint, redirect, url_for, flash
from flask import render_template, g
from app import db
from flask_login import login_required
from .forms import CheckInForm, CheckIn_Users, Checkout
from apps.Machine.models import tool_User

Tool_View = Blueprint('Tool_View', __name__)

@Tool_View.route('/checkIn', methods=['get', 'post'])
@login_required
def CheckIn():
    template = "ToolCheckIn/CheckInTable.html"
    title = "Check In Table"
    CheckInUser = tool_User.query.all()



    return render_template(template, title=title, CheckInUser=CheckInUser)

@Tool_View.route('/checkInForm', methods=['get', 'post'])
@login_required
def CheckInSignIn():
    title = "Check In Table"
    form =CheckInForm()
    if form.validate_on_submit():

        toolUser = tool_User(first_name=form.first_name.data, last_name=form.last_name.data,email=form.email.data,
                             tool=form.tool.data)
        db.session.add(toolUser)
        db.session.commit()
        flash('Your Check In Was Successfuly made', 'success')
        return redirect(url_for('Tool_View.CheckIn'))

    return render_template("ToolCheckIn/CheckInForm.html", title=title, form=form)
@Tool_View.route('/checkout/<CheckOut_id>', methods=['get', 'post'])
@login_required
def Checkout(CheckOut_id):
    tool_User.query.filter_by(id=CheckOut_id).delete()
    flash('You have Checked Out', 'success')
    return redirect(url_for('Tool_View.CheckIn'))