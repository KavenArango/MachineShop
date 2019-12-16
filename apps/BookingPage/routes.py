from flask import Blueprint, render_template, request
from flask import Flask
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


@Booking_View.route('/booking/<machine_id>')
def Machine_Details(machine_id):
    template = "BookingPage/schedule.html"
    title = "Reserve"
    MachineName = machines.query.filter_by(id=machine_id).first()
    ball = machines.query.distinct(machines.machine_name).all()

    return render_template(template, title=title, ball=ball, MachineID=MachineName)


@Booking_View.route('/process', methods=['POST'])
def process():
    Block_ID = request.form['blockId']
    User_ID = request.form['User_ID']
    Machine_ID = request.form['Machine_ID']
    MachineBookingDate = request.form['MachineBookingTime']
    MachineBookingTime = request.form['MachineBookingDate']
    DateMachineBooked = request.form['DateMachineBooked']

    return 'Block ID:'

    # if Machine_ID and MachineBookingDate and MachineBookingTime and Block_ID and User_ID and DateMachineBooked:







