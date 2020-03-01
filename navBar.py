from flask_nav import Nav
from flask import app
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator
from app import nav
from flask_login import LoginManager, current_user

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
        Logout = View('Logout', 'login.logout')
        return Navbar(MachineShop, Home_view, Machine_Des, Booking_view, StudentSearch, RequestView, post,an, Logout)
    elif current_user.is_authenticated and current_user.user_type == 3:
        Logout = View('Logout', 'login.logout')
        checkIn = View('Check In Table', 'Tool_View.CheckIn')
        CheckInForm = View('Check In Form', 'Tool_View.CheckInSignIn')
        return Navbar( checkIn,CheckInForm,Logout )
    elif current_user.is_authenticated:
        MachineShop = View('Machine Shop', 'Main_View.home')
        Request = View('Level Request', 'Student_view.requests')
        post = View('Post', 'Student_view.post')
        Studend = View('Profile', 'Student_view.profile')
        Machine_Des = View('Machine Descriptions', 'Machine_View.Machine')
        Home_view = View('Home', 'Main_View.home')
        Booking_view = Subgroup('Booking',
                                View('Bridgeport', 'Booking_View.Machine_Details', machine_id='1'),
                                View('HAAS', 'Booking_View.Machine_Details', machine_id='2'),
                                View('Lathe', 'Booking_View.Machine_Details', machine_id='3'),
                                View('Syil', 'Booking_View.Machine_Details', machine_id='4'))
        Logout = View('Logout', 'login.logout')
        return Navbar(MachineShop, Home_view, Machine_Des, Booking_view, Request,Studend,post, Logout)

    else:
        login = View('Login', 'login.login_form')
        signup = View('Signup', 'login.signup')
        return Navbar(login, signup)



