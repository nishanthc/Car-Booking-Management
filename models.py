from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PasswordType, EmailType
from sqlalchemy import ForeignKey
from flask_login import UserMixin
from app import LoginManager
from flask_migrate import Migrate
import datetime
from datetime import timedelta
from app import app
from app import login_manager

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    email_notifications = db.Column(db.Boolean, default=True)
    text_notifications = db.Column(db.Boolean, default=True)
    date_enrolled = db.Column(db.DateTime, default=datetime.datetime.now)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ))
    email = db.Column(EmailType, unique=True, nullable=False)
    mobile = db.Column(db.String(80), nullable=True)
    admin = db.Column(db.Boolean, default=False)
    profile_complete = db.Column(db.Boolean, default=False)
    bookings = db.relationship('Booking', backref='user')
    def __repr__(self):
        return '<User %r>' % self.username


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String(80), unique=True, nullable=False)
    registration = db.Column(db.String(80), unique=True, nullable=False)
    make = db.Column(db.String(80), unique=True, nullable=False)
    model = db.Column(db.String(80), unique=True, nullable=False)
    bookings = db.relationship('Booking', backref='car')
    def __repr__(self):
        return '<Subject %r>' % self.vin

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    def __repr__(self):
        return '<Lesson %r>' % self.id
    def is_car_avaiable(self):
        within_another_bookings_timeslot = db.session.query(Booking).filter(Booking.car_id == self.car_id,
            Booking.start_time <= self.start_time,Booking.end_time >= self.end_time).count()

        user_same_time_slot = db.session.query(Booking).filter(Booking.user_id == self.user_id,
                                                                            Booking.start_time <= self.start_time,
                                                                            Booking.end_time >= self.end_time).count()


        booking_within_this_range = db.session.query(Booking).filter(Booking.car_id == self.car_id,
            Booking.start_time >= self.start_time,Booking.end_time <= self.end_time).count()


        starts_two_hours_before_end_start = db.session.query(Booking).filter(Booking.car_id == self.car_id,
             Booking.end_time >= self.start_time - timedelta(hours=2),Booking.end_time <= self.start_time).count()

        print("In Range:", user_same_time_slot)
        print("In Range:",within_another_bookings_timeslot)
        print("Out of Range:",booking_within_this_range )
        print("starts two hours before an end:", starts_two_hours_before_end_start)




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
