from flask import Flask, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)


app.config['SECRET_KEY'] = 'KILLME'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://MachineShop:KAVENSTEVESHANNONALLDUMB@25.78.65.33/machineshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from apps.Hompage.routes import Main_View
from apps.StudentPage.routes import Student_view
from apps.accounts.routes import login_view
from apps.StaffPage.routes import Staff_View
from apps.Machine.routes import Machine_View
from apps.BookingPage.routes import Booking_View
from apps.AdminBookingPage.routes import admin_booking_View
from apps.ToolCheckIn.routes import Tool_View
from flask_bootstrap import Bootstrap


app.register_blueprint(Main_View)
app.register_blueprint(Student_view)
app.register_blueprint(login_view)
app.register_blueprint(Staff_View)
app.register_blueprint(Machine_View)
app.register_blueprint(Booking_View)
app.register_blueprint(admin_booking_View)
app.register_blueprint(Tool_View)


from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator
from apps.Machine.models import machines

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_type == 2
    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated :
            return redirect(url_for('Main_View.home'))
        else:
            return redirect(url_for('login.login_form'))

bootstrap = Bootstrap(app)
admin = Admin(app, index_view=MyAdminIndexView(), template_mode="bootstrap3")
nav = Nav(app)

from apps.accounts.models import Users
from apps.accounts.models import Users
from apps.Machine.models import machines, machine_image, machine_shop_map, machine_type
from apps.BookingPage.models import Booking
from apps.StaffPage.models import Request, Post
from apps.Admin.routes import MyAdminView

@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)


@nav.navigation('my_nav')
def create_nav():

    if current_user.is_authenticated and current_user.user_type == 1:
        StudentSearch = View('Student Search', 'Staff_View.student_search')
        RequestView = View('Student Requests', 'Staff_View.request_search')
        MachineShop = View('Machine Shop', 'Main_View.home')
        an = View('Announcment', 'Staff_View.newPost')
        post = View('Post', 'Student_view.post')
        Machine_Des = View('Machine Descriptions', 'Machine_View.Machine')
        Home_view = View('Home', 'Main_View.home')
        admin_booking = View('admin booking', 'adminBooking_View.bookingpage')
        Booking_view = Subgroup('Booking', View('Bridgeport', 'Booking_View.Machine_Details', machine_id='1'),
                                View('HAAS', 'Booking_View.Machine_Details', machine_id='2'),
                                View('Lathe', 'Booking_View.Machine_Details', machine_id='3'),
                                View('Syil', 'Booking_View.Machine_Details', machine_id='4'))
        Logout = View('Logout', 'login.logout')
        return Navbar(MachineShop, Home_view, Machine_Des, Booking_view, StudentSearch, RequestView, post,an, Logout)
                      admin_booking, an, Logout)
    elif current_user.is_authenticated and current_user.user_type == 3:
        Logout = View('Logout', 'login.logout')
        checkIn = View('Check In Table', 'Tool_View.CheckIn')
        CheckInForm = View('Check In Form', 'Tool_View.CheckInSignIn')
        return Navbar( checkIn,CheckInForm,Logout )
    elif current_user.is_authenticated:
        MachineShop = View('Machine Shop', 'Main_View.home')
        Request = View('Level Request', 'Student_view.requests')
        post = View('Post', 'Student_view.post')
        admin_booking = View('admin booking', 'adminBooking_View.bookingpage')
        Studend = View('Profile', 'Student_view.profile')
        Machine_Des = View('Machine Descriptions', 'Machine_View.Machine')
        Home_view = View('Home', 'Main_View.home')
        Booking_view = Subgroup('Booking',
                                View('Bridgeport', 'Booking_View.Machine_Details', machine_id='1'),
                                View('HAAS', 'Booking_View.Machine_Details', machine_id='2'),
                                View('Lathe', 'Booking_View.Machine_Details', machine_id='3'),
                                View('Syil', 'Booking_View.Machine_Details', machine_id='4'))
        Logout = View('Logout', 'login.logout')
        return Navbar(MachineShop, Home_view, Machine_Des, Booking_view, Request, Studend, post,
                      admin_booking, Logout)

    else:
        login = View('Login', 'login.login_form')
        signup = View('Signup', 'login.signup')
        return Navbar(login, signup)


if __name__ == '__main__':
    app.run()
