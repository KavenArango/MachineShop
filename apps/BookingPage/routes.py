from flask import Blueprint
from flask import render_template
from apps.accounts.models import Users
from apps.StudentPage.models import Student, majors, Levels
from apps.Machine.models import machines
from apps.BookingPage.forms import BookingForm


Booking_View = Blueprint('Booking_View', __name__)


@Booking_View.route('/booking', methods=['POST', 'GET'])
def MachineSchedule():
    template = "BookingPage/schedule.html"
    title = "Reserve"
    return render_template(template, title=title)


@Booking_View.route('/MachineSchedule')
def MachineScheduleConfirm():
    template = "BookingPage/booking.html"
    title = "Confirm Booking"
    form = BookingForm()
    return render_template(template, title=title, form=form)




# @Booking_View.route('/booking', methods=['POST', 'GET'])
# def MachineSchedule():
#     template = "BookingPage/schedule.html"
#     title = "Reserve"
#     form = BookingForm()
#     Machine = MachineSchedule.query.filter(Student.user_id == Users.id).join(
#         Users, Users.id == Student.user_id
#     ).join(
#         machines, machines.id == Student.machine_id
#     ).join(
#         majors, majors.id == Student.major_id
#     ).join(
#         Levels, Levels.id == Student.level_id
#     ).with_entities(
#         Student.id.label("id"),
#         Users.first_name.label("first_name"),
#         Users.last_name.label("last_name"),
#         Users.email.label("email"),
#         majors.major_name.label("major_name"),
#         machines.machine_name.label("machine_name"),
#         Levels.description.label("level")
#     ).all()
#     return render_template(template, title=title, students=Machine, form=form)

