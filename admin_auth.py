from flask_admin import helpers, expose
import flask_admin as admin
import flask_login as login
from flask import Flask, url_for, redirect, render_template, request
class MyAdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        if login.current_user.is_authenticated:
            if login.current_user.admin:
                return super(MyAdminIndexView, self).index()
        return redirect(url_for('user_blueprint.login'))



