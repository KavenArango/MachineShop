import urllib.parse
from flask import Flask, redirect, url_for, request
from flask_bcrypt import Bcrypt
from flask_uploads import uploaded_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView



from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
import nexmo
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator








UPLOAD_FOLDER = "static/media"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}



app = Flask(__name__)

client = nexmo.Client(key="716ab2fb", secret="y5ZvDW0kP29dzzpa")



app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config['SECRET_KEY'] = 'KILLME'

url = URLSafeTimedSerializer(app.config['SECRET_KEY'])

params = urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};"
                                 "Server=tcp:idea-lab1.database.windows.net,1433;Database=machineshop;Uid=jsnow;"
                                 "Pwd=Kavensteveshannonalldumb!;Encrypt=yes;TrustServerCertificate=no;"
                                 "Connection Timeout=30;")
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEBUG'] =
app.config['MAIL_USERNAME'] = "idea.lab.snhu@gmail.com"
app.config['MAIL_PASSWORD'] = "Clownpictures"
app.config['MAIL_DEFAULT_SENDER'] = "idea.lab.snhu@gmail.com"
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_SUPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False


mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)



from apps.Machine import models
from apps.BookingPage.models import Booking
from apps.StaffPage.models import Request, Post
from apps.Hompage.routes import Main_View
from apps.StudentPage.routes import Student_view
from apps.accounts.routes import login_view
from apps.StaffPage.routes import Staff_View
from apps.Machine.routes import Machine_View
from apps.BookingPage.routes import Booking_View
from apps.AdminBookingPage.routes import admin_booking_View
from apps.ToolCheckIn.routes import Tool_View
app.register_blueprint(Main_View)
app.register_blueprint(Student_view)
app.register_blueprint(login_view)
app.register_blueprint(Staff_View)
app.register_blueprint(Machine_View)
app.register_blueprint(Booking_View)
app.register_blueprint(admin_booking_View)
app.register_blueprint(Tool_View)



class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_type == 2

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated :
            return redirect(url_for('Main_View.home'))
        else:
            return redirect(url_for('login.login_form'))

admin = Admin(app, index_view=MyAdminIndexView(), template_mode="bootstrap3")






bootstrap = Bootstrap(app)
nav = Nav(app)
@nav.navigation('my_nav')
def my_nav():

    if current_user.is_authenticated and current_user.user_type == 1:
        StudentSearch = View('Student Search', 'Staff_View.student_search')
        RequestView = View('Student Requests', 'Staff_View.request_search')
        MachineShop = View('Machine Shop', 'Main_View.home')
        an = View('Announcment', 'Staff_View.newPost')
        post = View('Post', 'Student_view.post')
        Machine_Des = View('Machine Descriptions', 'Machine_View.Machine')
        Home_view = View('Home', 'Main_View.home')
        Booking_view = Subgroup('Booking', View('Bridgeport', 'Booking_View.Machine_Details', machine_id='1'),
                                View('HAAS', 'Booking_View.Machine_Details', machine_id='2'),
                                View('Lathe', 'Booking_View.Machine_Details', machine_id='3'),
                                View('Syil', 'Booking_View.Machine_Details', machine_id='4'))
        admin_view = View("Admin booking", "adminBooking_View.bookingpage")
        Logout = View('Logout', 'login.logout')
        return Navbar(MachineShop, Home_view, Machine_Des, Booking_view, StudentSearch, RequestView, post,an,admin_view, Logout)
    elif current_user.is_authenticated and current_user.user_type == 3:
        Logout = View('Logout', 'login.logout')
        checkIn = View('Check In Table', 'Tool_View.CheckIn')
        CheckInForm = View('Check In Form', 'Tool_View.CheckInSignIn')
        return Navbar( checkIn,CheckInForm,Logout )
    elif current_user.is_authenticated and current_user.user_type == 0:
        MachineShop = View('Machine Shop', 'Main_View.home')
        Request = View('Level Request', 'Student_view.requests')
        post = View('Post', 'Student_view.post')
        Studend = View('Profile', 'Student_view.profile')
        Machine_Des = View('Machine Descriptions', 'Machine_View.Machine')
        Home_view = View('Home', 'Main_View.home')
        admin_view = View("Admin booking", "adminBooking_View.bookingpage")
        Booking_view = Subgroup('Booking',
                                View('Bridgeport', 'Booking_View.Machine_Details', machine_id='1'),
                                View('HAAS', 'Booking_View.Machine_Details', machine_id='2'),
                                View('Lathe', 'Booking_View.Machine_Details', machine_id='3'),
                                View('Syil', 'Booking_View.Machine_Details', machine_id='4'))
        Logout = View('Logout', 'login.logout')
        return Navbar(MachineShop, Home_view, Machine_Des, Booking_view, Request,Studend,post,admin_view, Logout)

    else:
        login = View('Login', 'login.login_form')
        signup = View('Signup', 'login.signup')
        return Navbar(login, signup)


from apps.accounts.models import Users
@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
