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
from apps.BookingPage.forms import BookingForm, BuildingSelect
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

    MachineName = models.machines.query.filter_by(id=machine_id).first()
    ball = models.machines.query.distinct(models.machines.machine_name).all()
    stick = Booking.query.filter(Booking.machine_id == machine_id).with_entities(
        Booking.Key.label("key")
    ).all()
    jsonStick = json.dumps(stick)
    # print(stick)
    # print(jsonStick)

    # print.pprint(jsonStick)
    return render_template(template, title=title, ball=ball, stick=stick, MachineID=MachineName, jsonStick=jsonStick)



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


@Booking_View.route('/booking/RoomSelection', methods=['get', 'post'])
@login_required
def buildings():
    template = "BookingPage/BuildingSelect.html"
    form = BuildingSelect()
    form.buildings.choices = [("-1", "")]
    form.buildings.choices += [(build.id, build.building_name) for build in
                              models.building.query.distinct(models.building.building_name).all()]
    form.rooms.choices = [("-1", "")]

    if (form.rooms.data != "None" and form.buildings.data != "None") and (form.rooms.data != -1 and form.buildings.data != -1):
        return redirect(url_for('Booking_View.Maps', building_id=form.buildings.data, room_id=form.rooms.data))
    return render_template(template, form=form)


# @Booking_View.route('/booking/RoomSelection', methods=['get', 'post'])
# @login_required
# def buildings():
#     template = "BookingPage/BuildingSelect.html"
#     form = BuildingSelect()
#     form.buildings.choices = [("-1", "")]
#     form.buildings.choices += [(build.id, build.building_name) for build in
#                               models.building.query.distinct(models.building.building_name).all()]
#     form.rooms.choices = [("-1", "")]
#
#     if (form.rooms.data != "None" and form.buildings.data != "None") and (form.rooms.data != -1 and form.buildings.data != -1):
#         return redirect(url_for('adminBooking_View.Maps', room_id=form.rooms.data))
#     return render_template(template, form=form)


@Booking_View.route('/booking/RoomSelection/MachineSelection/<room_id>', methods=['get', 'post'])
@login_required
def Maps(room_id):
    template = "BookingPage/Map.html"
    MachineMap = models.machine_join.query.all()
    currentRoom = models.room.query.filter_by(id=room_id).first()
    Machine_Images = models.machine_image.query.all()
    return render_template(template, MachineMaps=MachineMap, Room=currentRoom, Machine_Images=Machine_Images)

