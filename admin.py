from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user
from forms import RegistrationForm, LoginForm
from init import app
from models import db, User

admin = Blueprint('admin',__name__)


@admin.route('/admin', methods=('GET', 'POST'))
def home():
    if current_user.admin:
        return render_template('admin/home.html', title='Admin')
    return '', 403


if __name__ == '__main__':
    app.run()
