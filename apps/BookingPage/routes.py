from flask import Blueprint
from flask import render_template
from app import db
from apps.accounts.models import Users
from apps.StudentPage.models import Student, majors, Levels
from apps.Machine.models import machines
from apps.BookingPage.models import Booking, GroupJoin
from apps.BookingPage.forms import BookingForm
from datetime import datetime


Booking_View = Blueprint('Booking_View', __name__)


@Booking_View.route('/booking')
def MachineSchedule():
    template = "BookingPage/schedule.html"
    title = "Reserve"
    MachineName = "Machine"
    ball = machines.query.distinct(machines.machine_name).all()
    return render_template(template, title=title, ball=ball, MachineID=MachineName)


@Booking_View.route('/MachineSchedule/<machine_id>')
def MachineScheduleConfirm(machine_id):
    template = "BookingPage/booking.html"
    title = "Confirm Booking"
    form=BookingForm()
    bookings = Student.query.distinct(Users.email).group_by(Users.email).filter(Student.user_id == Users.id).join(
        Users, Users.id == Student.user_id
    ).join(
        machines, machines.id == Student.machine_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        Student.id.label("id"),
        Users.first_name.label("first_name"),
        Users.last_name.label("last_name"),
        Users.email.label("email"),
        machines.machine_name.label("machine_name"),
        Levels.description.label("level")
    ).all()
    return render_template(template, title=title, form=form, booking=bookings)


@Booking_View.route('/booking/<machine_id>')
def Machine_Details(machine_id):
    template = "BookingPage/schedule.html"
    title = "Reserve"
    ball = machines.query.distinct(machines.machine_name).all()
    MachineName = machines.query.filter_by(id=machine_id).first()
    return render_template(template, title=title,ball=ball, MachineID=MachineName)

