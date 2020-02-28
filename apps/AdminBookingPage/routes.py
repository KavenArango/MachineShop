import os
from app import ALLOWED_EXTENSIONS, uploaded_file, app
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from apps.Machine.models import building, room, machine_image
from flask import Blueprint
from flask import render_template
from flask_login import current_user, login_required


admin_booking_View = Blueprint('adminBooking_View', __name__)




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@admin_booking_View.route('/adminbooking', methods=['GET', 'POST'])
@login_required
def bookingpage():
    template = "adminBookingPage/adminBookingPage.html"
    if request.method == 'POST':
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
            return redirect(url_for('uploaded_file', filename=filename))

    return render_template(template)


@app.route('/adminbooking/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



