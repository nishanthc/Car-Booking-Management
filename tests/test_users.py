import os
import unittest
from init import app
from models import db, User
from flask import url_for


TEST_DB = 'test2.db'

class UsersTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(app.root_path, TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    # executed after each test
    def tearDown(self):
        pass

    ###############
    #### tests ####
    ###############

    def test_registration_page(self):
        client = app.test_client()
        res = client.get('/register')
        assert res.status_code == 200

    def test_login_page(self):
        client = app.test_client()
        res = client.get('/login')
        assert res.status_code == 200


    def test_user_registration_login(self):
        client = app.test_client()
        registration_data = {'username': 'test',
                'email': 'test@test.com',
                'mobile': '07910244279',
                'password': 'password1',
                'confirm_password': 'password1'}
        res = client.post('/register',
                          data=registration_data)
        # Assert that the user was redirected to the login page
        assert res.status_code == 302

        user = User.query.filter_by(username=registration_data['username'],
                                    email=registration_data['email'],
                                    mobile=str(0)+registration_data['mobile']).first()

        # Assert that the user was found
        self.assertTrue(user)

        # Assert that the password recieved the same hash
        self.assertTrue(user.password == registration_data['password'])

        client = app.test_client()
        login_data = {'username': registration_data['username'],
                'password': registration_data['password']}

        res = client.post('/login',
                          data=login_data)
        # Assert that the user was redirected to the home
        assert res.status_code == 302


        with client.session_transaction() as sess:
            user_id = sess['user_id']

        # Assert that a session has been created for the user
        assert user_id == "1"








if __name__ == "__main__":
    unittest.main()
