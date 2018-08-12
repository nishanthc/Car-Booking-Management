from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PasswordType,EmailType
from flask_login import UserMixin
from init import app
from init import login_manager
from flask_migrate import Migrate
db = SQLAlchemy(app)
import datetime

migrate = Migrate(app, db)
class User(UserMixin,db.Model):
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
    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)