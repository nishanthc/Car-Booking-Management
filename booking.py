from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user
from forms import RegistrationForm, LoginForm, ProfileForm
from init import app
from models import db, User
from user import *

booking = Blueprint('booking',__name__)



@booking.route('/bookings', methods=('GET', 'POST'))
def bookings():
    if not current_user.is_authenticated:
        return redirect(url_for('core.home'))

    return render_template('booking/dashboard.html', title='Bookings')




if __name__ == '__main__':
    app.run()
