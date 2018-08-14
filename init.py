from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
db_file_name = "tbs.db"
test_db_file_name = "test_database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(app.root_path, db_file_name)
app.config['TEST_SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(app.root_path, test_db_file_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'fsdfsdfdsf'
db.create_all()
from core import core
from admin import admin
from users import users
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(admin)
csrf = CSRFProtect(app)

if __name__ == '__main__':
    app.run()