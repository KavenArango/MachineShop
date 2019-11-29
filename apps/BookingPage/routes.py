from flask import Blueprint
from flask import render_template

from apps.BookingPage.forms import BookingForm

Booking_View = Blueprint('Booking_View', __name__)

@Booking_View.route('/booking')
def MachineSchedule():
    template = "BookingPage/booking.html"
    title = "Reserve"
    form = BookingForm()
    return render_template(template, title=title, form=form)

@Booking_View.route('/bridgeport')
def Bridgeport():
    machine = "Bridgeport"
    template = "BookingPage/schedule.html"
    return render_template(template, value=machine)

@Booking_View.route('/cnc')
def CNC():
    machine = "CNC"
    template = "BookingPage/schedule.html"
    return render_template(template, value=machine)

@Booking_View.route('/lathe')
def Lathe():
    machine = "Lathe"
    template = "BookingPage/schedule.html"
    return render_template(template, value=machine)

@Booking_View.route('/syil')
def Syil():
    machine = "Syil"
    template = "BookingPage/schedule.html"
    return render_template(template, value=machine)

@Booking_View.route('/extra')
def Extra():
    machine = "extra"
    template = "BookingPage/schedule.html"
    return render_template(template, value=machine)
