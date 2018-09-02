from flask_wtf import FlaskForm
from models import User, Car
from wtforms import StringField, PasswordField, IntegerField, validators, BooleanField, SelectField,DateTimeField
from wtforms.validators import DataRequired
from wtforms_alchemy import Unique, ModelForm


class RegistrationForm(ModelForm, FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Unique(User.username,
                                                          message="User with username exists")])

    email = StringField('Email', validators=[DataRequired(),
                                             validators.Email(message="Must be a valid email address"),
                                             Unique(User.email, message="User with email exists")])

    mobile = IntegerField('Mobile', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired(),
                                                     validators.EqualTo('confirm_password',
                                                                        message='Passwords must match')])
    confirm_password = PasswordField('Repeat Password')


class ProfileForm(ModelForm, FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Unique(User.username,
                                                          message="User with username exists")])

    email = StringField('Email', validators=[DataRequired(),
                                             validators.Email(message="Must be a valid email address"),
                                             Unique(User.email, message="User with email exists")])

    mobile = IntegerField('Mobile', validators=[DataRequired()])
    first_name =  StringField('First Name',validators=[DataRequired()])
    last_name = StringField('First Name',validators=[DataRequired()])
    email_notifications = BooleanField('Email Notifications')
    text_notifications = BooleanField('Text Notifications')

class BookingForm(ModelForm, FlaskForm):

    cars = Car.query.all()
    car_list = []
    #car.id, car.make + car.model
    for car in cars:
        car_make_model = car.make + " " + car.model
        car_list.append((car.id,car_make_model ))
    car_id = SelectField('Car',choices=car_list, validators=[DataRequired()])


    start_date_time = DateTimeField('Start Date/Time', id="start_date_time",format='%Y-%m-%d %H:%M:%S',validators=[DataRequired()])
    end_date_time = DateTimeField('End Date/Time',id="end_date_time", format='%Y-%m-%d %H:%M:%S',validators=[DataRequired()])



class LoginForm(ModelForm, FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
