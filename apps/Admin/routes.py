from flask import Flask, redirect, url_for, request, flash
from flask_admin import BaseView, expose, AdminIndexView, Admin
from flask_admin.actions import action
from flask_admin.babel import gettext, ngettext
from flask_admin.contrib import sqla
from flask_login import login_user, current_user, logout_user, login_required
from app import admin, db
from flask_admin.contrib.sqla import ModelView
from apps.accounts.models import Users
from apps.Machine.models import machines,machine_type,machine_image,machine_shop_map, room
from apps.BookingPage.models import Booking
from apps.StaffPage.models import Request,Post, Request_Des

class MyAdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_type == 2
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login.login_form'))
class test(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_type == 2
    @expose('/')
    def index(self):
        return self.render('AdminViews/Test.html')

admin.add_view(test(name='Test', endpoint='test'))

class User(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_type == 2
    column_exclude_list = ['password', ]
    #can_edit = False
    column_searchable_list = ['first_name', 'email', 'last_name']
    list_template = 'AdminViews/user_edit.html'
    column_editable_list = ['user_type']
    page_size = 20


class Machines(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_type == 2


class Posts(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_type == 2
    can_edit = False

class MachineType(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_type == 2
    can_edit = False


class RequestView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_type == 2


admin.add_view(User(Users, db.session))
admin.add_view(Machines(machines,db.session))
admin.add_view(MyAdminView(Booking,db.session))
admin.add_view(RequestView(Request,db.session))
admin.add_view(MyAdminView(Request_Des,db.session))
admin.add_view(Posts(Post,db.session))
admin.add_view(MachineType(machine_type, db.session))
admin.add_view(MyAdminView(machine_image,db.session))
admin.add_view(MyAdminView(machine_shop_map,db.session))
admin.add_view(MyAdminView(room,db.session))