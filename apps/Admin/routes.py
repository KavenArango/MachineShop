from flask import Flask, redirect, url_for, request, flash
from flask_admin import BaseView, expose, AdminIndexView, Admin
from flask_admin.actions import action
from flask_admin.babel import gettext, ngettext
from flask_admin.contrib import sqla
from flask_login import login_user, current_user, logout_user, login_required
from app import db, admin
from apps.accounts.models import Users
from apps.Machine import models
from apps.BookingPage.models import Booking
from apps.StaffPage.models import Request, Post, Request_Des
from flask_admin.contrib.sqla import ModelView



