import os
import secrets
from PIL import Image
from app import ALLOWED_EXTENSIONS, uploaded_file, app, db
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from apps.Machine import models
from apps.Machine.models import building, room
from flask import Blueprint, jsonify
from flask import render_template, session
from flask_login import current_user, login_required
from apps.AdminBookingPage.forms import RoomForm, BuildingSelect


admin_booking_View = Blueprint('adminBooking_View', __name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@admin_booking_View.route('/adminbooking', methods=['get', 'post'])
@login_required
def bookingpage():
    template = "adminBookingPage/adminBookingPage.html"
    Buildings = models.building.query.distinct(models.building.building_name).all()

    if request.method == 'POST':
        print(request.files)
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #       TELL USER IMAGE HAS BEEN SENT
    return render_template(template, Buildings=Buildings)


@admin_booking_View.route('/adminbooking/<building_id>', methods=['get', 'post'])
def building_state(building_id):
    template = "adminBookingPage/RoomEdit.html"
    Rooms = models.room.query.filter_by(building_id=building_id).all()
    roomArray = []

    for rooms in Rooms:
        roomObj = {}
        roomObj['id'] = rooms.id
        roomObj['Number'] = rooms.room_num
        roomArray.append(roomObj)

    return jsonify({'Room': roomArray})


@admin_booking_View.route('/adminbooking/building/<building_id>/<room_id>', methods=['get', 'post'])
@login_required
def room(building_id, room_id):
    template = "adminBookingPage/RoomEdit.html"
    Rooms = models.room.query.distinct(models.room.room_num).all()
    currentRoom = models.room.query.filter_by(id=room_id).first()
    Building = models.building.query.filter_by(id=building_id).first()
    Machine =  models.machines.query.all()
    Machine_Images = models.machine_image.query.all()
    return render_template(template, Rooms=Rooms, Building=Building, currentRoom=currentRoom, machines=Machine,
                           machineImages=Machine_Images)



@admin_booking_View.route('/adminbooking/room/creation', methods=['get', 'post'])
@login_required
def roomcreation():
    form = RoomForm()
    template = "adminBookingPage/createRoom.html"
    form.Building.choices = [(m.id, m.building_name) for m in
                             models.building.query.distinct(models.building.building_name).all()]
    Room = models.room.query.distinct(models.room.room_num).all()
    # Buildings = models.building.building_name
    if form.validate_on_submit():
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            newroom = models.room(room_num=form.RoomNum.data, room_image=filename, building_id=form.Building.data)
            db.session.add(newroom)
            db.session.commit()
            return redirect(url_for('adminBooking_View.buildings'))
    return render_template(template, form=form)




@admin_booking_View.route('/adminbooking/building', methods=['get', 'post'])
@login_required
def buildings():
    template = "adminBookingPage/Building.html"
    form = BuildingSelect()
    form.buildings.choices = [("-1", "")]
    form.buildings.choices += [(build.id, build.building_name) for build in
                              models.building.query.distinct(models.building.building_name).all()]
    form.rooms.choices = [("-1", "")]

    print(form.buildings.data)
    print(form.rooms.data)

    if (form.rooms.data != "None" and form.buildings.data != "None") and (form.rooms.data != -1 and form.buildings.data != -1):
        return redirect(url_for('adminBooking_View.room', building_id=form.buildings.data, room_id=form.rooms.data))
    return render_template(template, form=form)

@admin_booking_View.route('/add', methods=['post'])
def add():
    data = request.get_json()
    xpose = data['xpose']
    ypose = data['ypose']
    machine_id = data['machine_id']
    room = data['current_room']

    machine_map = models.machine_join(x_pose=xpose,y_pose=ypose,machine_id=machine_id,room=room)
    db.session.add(machine_map)
    db.session.commit()

    return jsonify({'result': 'Saved', 'xpose':xpose, 'ypose': ypose, 'machine_id': machine_id, 'room_id': room})