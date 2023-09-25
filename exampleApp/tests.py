from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from exampleProject.settings import firestore
import json


def get_token(self):
    response = self.client.post('/login', data=json.dumps({
        "email": "rsuarezdavid@gmail.com",
        "password": "16febrero"
    }), content_type='application/json')
    return response.data['token']


class JobTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    ########################################### GETS ###########################################

    ########################################### 200 OK ###########################################

    def test_get_all_jobs(self):
        response = self.client.get('/jobs')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_job_by_id(self):
        uid = firestore.collection(u'jobs').where(
            u'company', u'==', u'Cruz-Brown').get()[0].id
        response = self.client.get(f'/jobs/{uid}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_jobs_with_pagination(self):
        response = self.client.get('/jobs?page=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    ########################################### 400 TYPE HTTP ERRORS ###########################################

    def test_get_job_by_id_not_found(self):
        response = self.client.get('/jobs/123456789')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"error": "Job not found"})

    def test_get_jobs_with_pagination_page_less_than_1(self):
        response = self.client.get('/jobs?page=0')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"error": "Page must be greater or equal than 1"})

    def test_get_jobs_with_pagination_page_not_integer(self):
        response = self.client.get('/jobs?page=abc')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"error": "Page must be an integer"})

    ########################################### POST ###########################################

    ########################################### 201 CREATED ###########################################

    def test_post_job(self):
        headers = {'Bearer': f'Bearer {get_token(self)}'}
        data = {
            "company": "Test Company",
            "title": "Test Title",
            "location": "Test Location"
        }
        response = self.client.post(
            '/jobs', data=json.dumps(data), content_type='application/json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {"message": "Job added successfully"})

    ########################################### 400 BAD REQUESTS ###########################################

    def test_post_job_without_token(self):
        data = {
            "company": "Test Company",
            "title": "Test Title",
            "location": "Test Location"
        }
        response = self.client.post(
            '/jobs', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
                         "error": "Token login is missing, you must login first and put the token on the header request"})

    def test_post_job_without_company(self):
        headers = {'Bearer': f'Bearer {get_token(self)}'}
        data = {
            "title": "Test Title",
            "location": "Test Location",
            "company": ""
        }
        response = self.client.post(
            '/jobs', data=json.dumps(data), content_type='application/json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
                         "error": "company must have more than 3 characters"})

    def test_post_job_without_title(self):
        headers = {'Bearer': f'Bearer {get_token(self)}'}
        data = {
            "company": "Test Company",
            "location": "Test Location",
            "title": ""
        }
        response = self.client.post(
            '/jobs', data=json.dumps(data), content_type='application/json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
                         "error": "title must have more than 3 characters"})

    def test_post_job_without_location(self):
        headers = {'Bearer': f'Bearer {get_token(self)}'}
        data = {
            "company": "Test Company",
            "title": "Test Title",
            "location": ""
        }
        response = self.client.post(
            '/jobs', data=json.dumps(data), content_type='application/json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
                         "error": "location must have more than 3 characters"})
