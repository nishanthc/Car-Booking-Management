from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user
from forms import RegistrationForm, LoginForm
from init import app
from models import db, User

core = Blueprint('core',__name__)
@core.route('/')
def home():
    return render_template('home.html', title='Hello!')



