from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import json
from exampleApp.firebase import auth, db as firestore


def get_token(self):
    response = self.client.post('/login', data=json.dumps({
        "email": "test@gmail.com",
        "password": "password"
    }), content_type='application/json')
    return response.data['token']


def delete_auth_user(self):
    auth.delete_user_account(get_token(self))


def delete_data_user(self):
    user = auth.get_account_info(get_token(self))
    firestore.collection(u'users').document(
        user["users"][0]["localId"]).delete()


class RegisterTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    ########################################### 201 CREATED ###########################################

    def test_register_user(self):
        response = self.client.post('/register', data=json.dumps({
            "name": "Test",
            "last_name": "Test",
            "phone": "628074491",
            "email": "test@gmail.com",
            "password": "password"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        delete_data_user(self)
        delete_auth_user(self)

    ########################################### 400 BAD REQUESTS ###########################################

    def test_register_user_with_invalid_email(self):
        response = self.client.post('/register', data=json.dumps({
            "name": "Test",
            "last_name": "Test",
            "phone": "628074491",
            "email": "testgmail.com",
            "password": "password"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"error": "email malformed"})

    def test_register_user_with_invalid_phone(self):
        response = self.client.post('/register', data=json.dumps({
            "name": "Test",
            "last_name": "Test",
            "phone": "6280744911",
            "email": "test@gmail.com",
            "password": "password"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"error": "phone malformed"})

    def test_register_user_with_invalid_name(self):
        response = self.client.post('/register', data=json.dumps({
            "name": "Te",
            "last_name": "Test",
            "phone": "628074491",
            "email": "test@gmail.com",
            "password": "password"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"error": "name must have more than 3 characters"})

    def test_register_user_with_invalid_last_name(self):
        response = self.client.post('/register', data=json.dumps({
            "name": "Test",
            "last_name": "Te",
            "phone": "628074491",
            "email": "test@gmail.com",
            "password": "password"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"error": "lastName must have more than 3 characters"})


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    ########################################### 400 BAD REQUESTS ###########################################

    def test_login_user_with_invalid_email(self):
        response = self.client.post('/login', data=json.dumps({
            "email": "testgmail.com",
            "password": "password"
        }), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
