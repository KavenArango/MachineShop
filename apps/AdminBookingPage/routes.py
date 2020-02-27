from flask import Blueprint
from flask import render_template
from flask_login import current_user, login_required


admin_booking_View = Blueprint('adminBooking_View', __name__)


@admin_booking_View.route('/adminbooking')
@login_required
def bookingpage():
    template = "adminBookingPage/adminBookingPage.html"
    return render_template(template)





