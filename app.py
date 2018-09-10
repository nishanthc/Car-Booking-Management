from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
import os

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db_file_name = "tbs.db"
test_db_file_name = "test_database.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(app.root_path, db_file_name)
app.config['TEST_SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(app.root_path, test_db_file_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'fsdfsdfdsf'



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
import user
from models import Booking, User as UserModel, Car, db

from admin_auth import MyAdminIndexView
admin = Admin(app, name='Electric Care Hire',index_view=MyAdminIndexView(), template_mode='bootstrap3')
admin.add_view(user.MyModelView(UserModel, db.session))
admin.add_view(user.MyModelView(Car, db.session))
admin.add_view(ModelView(Booking, db.session))






db.create_all()
from core import core
from booking import booking
from user import user
app.register_blueprint(core)
app.register_blueprint(booking)
app.register_blueprint(user)

csrf = CSRFProtect(app)
