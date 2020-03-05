from flask import Flask, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail


app = Flask(__name__)


app.config['SECRET_KEY'] = 'KILLME'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://MachineShop:KAVENSTEVESHANNONALLDUMB@25.78.65.33/machineshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEBUG'] =
app.config['MAIL_USERNAME'] = "idea.lab.snhu@gmail.com"
app.config['MAIL_PASSWORD'] = "Coronavirus"
app.config['MAIL_DEFAULT_SENDER'] = "idea.lab.snhu@gmail.com"
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_SUPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False


mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)



from apps.Hompage.routes import Main_View
from apps.StudentPage.routes import Student_view
from apps.accounts.routes import login_view
from apps.StaffPage.routes import Staff_View
from apps.Machine.routes import Machine_View
from apps.BookingPage.routes import Booking_View
from apps.ToolCheckIn.routes import Tool_View
from flask_bootstrap import Bootstrap


app.register_blueprint(Main_View)
app.register_blueprint(Student_view)
app.register_blueprint(login_view)
app.register_blueprint(Staff_View)
app.register_blueprint(Machine_View)
app.register_blueprint(Booking_View)
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
from navBar import my_nav
nav.register_element('my_nav', my_nav)
from apps.accounts.models import Users
from apps.accounts.models import Users
from apps.Machine.models import machines, machine_image, machine_shop_map , machine_type
from apps.BookingPage.models import Booking
from apps.StaffPage.models import Request, Post
from apps.Admin.routes import MyAdminView

@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)




if __name__ == '__main__':
    app.run()
