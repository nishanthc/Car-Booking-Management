from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user
from forms import RegistrationForm, LoginForm
from app import app
from models import db, User
from user import *

core = Blueprint('core_blueprint',__name__)
@core.route('/')
def home():
    if current_user.is_authenticated:
        if is_profile_complete(current_user) == False:
            return redirect(url_for('user_blueprint.profile'))
        else:
            return render_template('home.html', title='Home')
    else:
        return render_template('home.html', title='Home')




