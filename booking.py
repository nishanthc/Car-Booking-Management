from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user
from forms import BookingForm
from init import app
from models import db, User, Booking
from user import *

booking = Blueprint('booking',__name__)

def user_has_booking():
    user = User.query.filter_by(id=current_user.id).first()
    user_bookings = Booking.query.filter_by(user_id=user.id).first()
    if user_bookings:
        return True
    else:
        return False

@booking.route('/bookings', methods=('GET', 'POST'))
def bookings():
    print(user_has_booking())
    if not current_user.is_authenticated:
        return redirect(url_for('core.home'))
    context = {"user_has_booking":user_has_booking}
    return render_template('booking/dashboard.html', title='Booking Dashboard',data=context)


@booking.route('/bookings/new', methods=('GET', 'POST'))
def new_booking():
    print(user_has_booking())
    if not current_user.is_authenticated:
        return redirect(url_for('core.home'))

    form = BookingForm()
    return render_template('booking/new.html', title='New Booking',form=form)



if __name__ == '__main__':
    app.run()
