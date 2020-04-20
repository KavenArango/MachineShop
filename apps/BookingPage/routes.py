import pprint

from flask import Blueprint, render_template, request, redirect, url_for, flash
import json
from flask import Flask
from flask_login import login_required, current_user

from app import db
from apps.accounts.models import Users
from apps.StudentPage.models import Student, majors, Levels
from apps.Machine import models
from apps.BookingPage.models import Booking
from flask_login import login_required, current_user
from apps.StudentPage.models import Notification
from apps.BookingPage.forms import BookingForm
from datetime import datetime


Booking_View = Blueprint('Booking_View', __name__)


@Booking_View.route('/booking/<machine_id>')
@login_required
def Machine_Details(machine_id):
    template = "BookingPage/schedule.html"
    title = "Reserve"
    if current_user.passed_exam < 0:
        flash('You Must Pass Safety Exam To Access Booking', 'success')
        return redirect(url_for('Main_View.home'))

    notifications = Notification.query.filter(Notification.user_id == current_user.id).all()
    MachineName = models.machines.query.filter_by(id=machine_id).first()
    ball = models.machines.query.distinct(models.machines.machine_name).all()
    stick = Booking.query.filter(Booking.machine_id == machine_id).with_entities(
        Booking.Key.label("key")
    ).all()
    jsonStick = json.dumps(stick)
    # print(stick)
    # print(jsonStick)

    # print.pprint(jsonStick)
    return render_template(template, title=title, ball=ball, stick=stick, MachineID=MachineName, jsonStick=jsonStick,
                          notifications=notifications)


@Booking_View.route('/process', methods=['POST'])
@login_required
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









