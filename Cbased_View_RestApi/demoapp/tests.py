# from django.test import TestCase

from rest_framework.test import APITestCase
from demoapp.models import Student

class StudentAPITestCase(APITestCase):
    def setUp(self):
        Student.objects.create(first_name= "aa",
                               last_name= "aaa",
                               roll_number= 7)

    def test_get_method(self):
        url='http://127.0.0.1:9000/student/'
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        obj=Student.objects.filter(first_name='aa') 
        self.assertEqual(obj.count(),1)
        print("GET method status code:",response.status_code)            

    def test_post_method_success(self):
        url='http://127.0.0.1:9000/student/'
        data={
        "first_name": "bsb",
        "last_name": "bbb",
        "roll_number": 90
        }
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,201)
        print("POST method status code Success:",response.status_code)

    def test_post_method_fail(self):
        url='http://127.0.0.1:9000/student/'
        data={
        "last_name": "bbb",
        "roll_number": 8
        }
        response=self.client.post(url,data,format='json')
        print("POST method status code Fail:",response.status_code)
        self.assertEqual(response.status_code,400)



    # def test_delete_method(self):
    #     url='http://127.0.0.1:9000/student/5/'
    #     response=self.client.delete(url)
    #     print("DELEETE method status code success:",response.status_code)
    #     self.assertEqual(response.status_code,204)
