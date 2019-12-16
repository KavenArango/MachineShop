from flask import Blueprint, render_template, request
from flask import Flask
from app import db
from apps.accounts.models import Users
from apps.StudentPage.models import Student, majors, Levels
from apps.Machine.models import machines
from apps.BookingPage.models import Booking
from apps.BookingPage.forms import BookingForm
from datetime import datetime


Booking_View = Blueprint('Booking_View', __name__)


@Booking_View.route('/booking/<machine_id>')
def Machine_Details(machine_id):
    template = "BookingPage/schedule.html"
    title = "Reserve"
    MachineName = machines.query.filter_by(id=machine_id).first()
    ball = machines.query.distinct(machines.machine_name).all()
    stick = Booking.query.distinct(Booking.Key).first()
    return render_template(template, title=title, ball=ball, MachineID=MachineName)


@Booking_View.route('/process', methods=['POST'])
def process():
    Block_ID = request.form['blockId']
    User_ID = request.form['User_ID']
    Machine_ID = request.form['Machine_ID']
    MachineBookingDate = request.form['MachineBookingTime']
    MachineBookingTime = request.form['MachineBookingDate']
    DateMachineBooked = request.form['DateMachineBooked']
    if request.method == "POST":
        book = Booking(Key=Block_ID, user_id=User_ID, machine_id=Machine_ID, booking_For_Date=MachineBookingTime,
                       Start_Time=MachineBookingDate, Booked_date=DateMachineBooked)
        db.session.add(book)
        db.session.commit()
    return 'Block ID:'









