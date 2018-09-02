from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user
from forms import RegistrationForm, LoginForm, ProfileForm
from init import app
from models import db, User

user = Blueprint('user',__name__)

def is_profile_complete(current_user):
    if current_user.profile_complete:
        return True
    else:
        return False

@user.route('/register', methods=('GET', 'POST'))
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
        return redirect(url_for('user.login'))

    return render_template('user/register.html', title='Register', form=form)


@user.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.home'))
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
    return render_template('user/login.html', title='Login', form=form)

@user.route('/profile', methods=('GET', 'POST'))
def profile():
    if current_user.is_authenticated == False:
        return redirect(url_for('core.home'))
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email_notifications = form.email_notifications.data
        user.text_notifications = form.text_notifications.data
        user.profile_complete = True
        db.session.commit()
        flash('Your details have been updated')
        return render_template('user/profile.html', title='Profile', form=form)
    return render_template('user/profile.html', title='Profile', form=form)




@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.home'))


if __name__ == '__main__':
    app.run()
