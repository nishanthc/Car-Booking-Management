from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user
from forms import BookingForm
from init import app
from models import db, User, Booking
from user import *

booking = Blueprint('booking_blueprint',__name__)

def user_has_booking():
    user_bookings = Booking.query.filter_by(user_id=current_user.id).count()

    if user_bookings > 0:
        return True
    else:
        return False


def get_user_bookings():
    user_bookings = Booking.query.filter_by(user_id=current_user.id)

    return user_bookings

@booking.route('/bookings', methods=('GET', 'POST'))
def bookings():

    if not current_user.is_authenticated:
        return redirect(url_for('core.home'))
    context = {"user_has_booking":user_has_booking(),"user_bookings":get_user_bookings()}
    return render_template('booking/dashboard.html', title='Booking Dashboard',data=context)


@booking.route('/bookings/new', methods=('GET', 'POST'))
def new_booking():
    if not current_user.is_authenticated:
        return redirect(url_for('core.home'))

    form = BookingForm()
    if form.validate_on_submit():
        print (form.car_id.data)
        booking = Booking(user_id=current_user.id,
                    car_id=form.car_id.data,
                    start_time=form.start_date_time.data,
                    end_time=form.end_date_time.data)
        db.session.add(booking)
        db.session.commit()
        flash('Thanks for making a booking')
        return redirect(url_for('booking.bookings'))
    return render_template('booking/new.html', title='New Booking',form=form)



if __name__ == '__main__':
    app.run()
