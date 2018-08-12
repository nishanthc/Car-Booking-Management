from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
import os
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from core import core
from users import users
app.register_blueprint(core)
app.register_blueprint(users)
csrf = CSRFProtect(app)
db_file_name = "test.db"
app.config['SECRET_KEY'] = 'fsdfsdfdsf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(app.root_path, db_file_name)

if __name__ == '__main__':
    app.run()