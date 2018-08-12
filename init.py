from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from core import core
from users import users
app.register_blueprint(core)
app.register_blueprint(users)
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = 'fsdfsdfdsf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/Nish/Development/Tutor_Booking_Management/test.db'

if __name__ == '__main__':
    app.run()