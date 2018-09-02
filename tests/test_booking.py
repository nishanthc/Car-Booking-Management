import unittest
from init import app
from models import db, User
import tests.test_user as test_user
class BookingTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['TEST_SQLALCHEMY_DATABASE_URI']
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    # executed after each test
    def tearDown(self):
        pass

    # functions

    def register_login_check_booking_dashboard(self):

        client = app.test_client()
        res = client.get('/profile')
        # Check if forbidden to none logged in users
        print(res.status_code)
        assert res.status_code == 200
    ###############
    #### tests ####
    ###############

    def test_booking_dashboard_not_logged_in(self):
        client = app.test_client()
        res = client.get('/bookings')
        # Check if forbidden to none logged in users
        assert res.status_code == 302

    def test_booking_dashboard_logged_in(self):


        test_user.UserTests.register(self)
        test_user.UserTests.login(self)










if __name__ == "__main__":
    unittest.main()
