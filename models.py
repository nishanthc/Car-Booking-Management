from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PasswordType, EmailType
from sqlalchemy import ForeignKey
from flask_login import UserMixin
from init import app
from init import login_manager
from flask_migrate import Migrate
import datetime
from init import db


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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
