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
from flask_nav.elements import Navbar,Subgroup,View,Link,Text,Separator

bootstrap = Bootstrap(app)

nav = Nav(app)


@nav.navigation('my_nav')
def create_nav():
    if current_user.is_authenticated:
        MachineShop = View('Machine Shop', 'Main_View.home')
        Machine_Des = View('Machine Descriptions', 'Machine_View.Machine')
        Home_view = View('Home', 'Main_View.home')
        Cnc_view = View('CNC Booking', 'Booking_View.CNC')
        Bridgeport_view = View('BridgePort Booking', 'Booking_View.Bridgeport')
        Lathe_view = View('Lathe Booking', 'Booking_View.Lathe')
        Syil_view = View('Syil Booking', 'Booking_View.Syil')
        Booking_view = Subgroup('Booking',
                                Cnc_view,
                                Bridgeport_view,
                                Lathe_view,
                                Syil_view)

        Logout = View('Logout', 'login.logout')
        return Navbar(MachineShop, Home_view, Machine_Des, Booking_view, Logout)
    else:
        login = View('Login', 'login.login_form')
        signup = View('Signup', 'login.signup')
        return Navbar(login, signup)




if __name__ == '__main__':
    app.run()


