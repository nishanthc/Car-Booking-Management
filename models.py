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
    email_notifcations = db.Column(db.Boolean, default=True)
    text_notifcations = db.Column(db.Boolean, default=True)
    date_enrolled = db.Column(db.DateTime, default=datetime.datetime.now)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ))
    email = db.Column(EmailType, unique=True, nullable=False)
    mobile = db.Column(db.Integer, nullable=True)
    admin = db.Column(db.Boolean, default=False)
    lessons = db.relationship('Lesson', backref='user')
    def __repr__(self):
        return '<User %r>' % self.username




class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=True)
    lessons = db.relationship('Lesson', backref='level')
    def __repr__(self):
        return '<Level %r>' % self.level

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    lessons = db.relationship('Lesson', backref='subject')
    def __repr__(self):
        return '<Subject %r>' % self.name

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    dateTime = db.Column(db.DateTime)
    paid = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Lesson %r>' % self.id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
