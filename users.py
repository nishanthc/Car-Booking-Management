from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user
from forms import RegistrationForm, LoginForm
from init import app
from models import db, User

users = Blueprint('users',__name__)


@users.route('/register', methods=('GET', 'POST'))
def register():
    if current_user.is_authenticated:
        return redirect(url_for('core.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    mobile=form.mobile.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@users.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        login_data = User(username=form.username.data,
                          password=form.password.data)
        user = User.query.filter_by(username=login_data.username.lower()).first()
        if user:
            if user.password == login_data.password.secret:
                login_user(user)
                return redirect(url_for('core.home'))
            else:
                flash('Invalid login')
        else:
            flash('Invalid login')
    return render_template('login.html', title='Login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.home'))


if __name__ == '__main__':
    app.run()
