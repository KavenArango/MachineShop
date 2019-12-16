from flask import Flask 
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user


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
from flask_bootstrap import Bootstrap


app.register_blueprint(Main_View)
app.register_blueprint(Student_view)
app.register_blueprint(login_view)
app.register_blueprint(Staff_View)
app.register_blueprint(Machine_View)
app.register_blueprint(Booking_View)


from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator
from apps.Machine.models import machines

bootstrap = Bootstrap(app)

nav = Nav(app)

from apps.accounts.models import Users


@nav.navigation('my_nav')
def create_nav():

    if current_user.is_authenticated and current_user.user_type == 1:
        StudentSearch = View('Student Search', 'Staff_View.student_search')
        RequestView = View('Student Requests', 'Staff_View.request_search')
        MachineShop = View('Machine Shop', 'Main_View.home')
        Post = View('Post', 'Staff_View.newPost')
        announcement = View('Announcement', 'Student_view.post')
        Machine_Des = View('Machine Descriptions', 'Machine_View.Machine')
        Home_view = View('Home', 'Main_View.home')
        Booking_view = Subgroup('Booking', View('Bridgeport', 'Booking_View.Machine_Details', machine_id='1'),
                                View('HAAS', 'Booking_View.Machine_Details', machine_id='2'),
                                View('Lathe', 'Booking_View.Machine_Details', machine_id='3'),
                                View('Syil', 'Booking_View.Machine_Details', machine_id='4'))
        Logout = View('Logout', 'login.logout')
        return Navbar(MachineShop, Home_view, Machine_Des, Booking_view, StudentSearch, RequestView,Post, announcement, Logout)
    elif current_user.is_authenticated:
        MachineShop = View('Machine Shop', 'Main_View.home')
        announcement = View('Announcement', 'Student_view.post')
        Request = View('Level Request', 'Student_view.requests')
        Machine_Des = View('Machine Descriptions', 'Machine_View.Machine')
        Home_view = View('Home', 'Main_View.home')
        Booking_view = Subgroup('Booking', View('Bridgeport', 'Booking_View.Machine_Details', machine_id='1'),
                                View('HAAS', 'Booking_View.Machine_Details', machine_id='2'),
                                View('Lathe', 'Booking_View.Machine_Details', machine_id='3'),
                                View('Syil', 'Booking_View.Machine_Details', machine_id='4'))
        Logout = View('Logout', 'login.logout')
        return Navbar(MachineShop, Home_view, Machine_Des, Booking_view, Request,announcement, Logout)

    else:
        login = View('Login', 'login.login_form')
        signup = View('Signup', 'login.signup')
        return Navbar(login, signup)


if __name__ == '__main__':
    app.run()
