import os
from app import ALLOWED_EXTENSIONS, uploaded_file, app
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from apps.Machine import models
from apps.Machine.models import building
from flask import Blueprint
from flask import render_template, session
from flask_login import current_user, login_required
from apps.AdminBookingPage.forms import Roomform


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


# @admin_booking_View.route('/adminbooking/room', methods=['get', 'post'])
# @login_required
# def room():
#     template = "adminBookingPage/RoomEdit.html"
#     room = models.room.query.distinct(models.room.room_num).all()
#     return render_template(template, Rooms=room)



@admin_booking_View.route('/adminbooking/building/<building_id>', methods=['get', 'post'])
@login_required
def building(building_id):
    template = "adminBookingPage/RoomEdit.html"
    Rooms = models.room.query.distinct(models.room.room_num).all()
    return render_template(template, Rooms=Rooms)




@admin_booking_View.route('/adminbooking/room/creation', methods=['get', 'post'])
@login_required
def roomcreation():
    form = Roomform()
    template = "adminBookingPage/createRoom.html"
    form.Building.choices = [(building.id, building.building_name) for building in building.query.all()]
    Room = models.room.query.distinct(models.room.room_num).all()
    # Buildings = models.building.building_name
    if form.validate_on_submit():
        # Room = models.room.query.distinct(models.room.room_num).all()
        return redirect(url_for('adminBooking_View.room'))
    return render_template(template, Rooms=Room, form=form)

