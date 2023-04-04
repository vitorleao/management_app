from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from manager.employee.models import Employee


class AllTestCase(APITestCase):

    def setUp(self):
        user = User.objects.create(username='user')
        user.set_password('user')
        user.save()
        self.client.force_authenticate(user=user)
        self.list_url = 'http://localhost:8000/employee/'
        self.employee1 = Employee.objects.create(
                    name='Jose da Silva',
                    email='jose.silva@email.com.br',
                    department='tester'
        )
        self.employee2 = Employee.objects.create(
                    name='Jose dos Santos',
                    email='jose.santos@email.com.br',
                    department='developer'
                    )

    def test_get_all(self):
        """Test GET to verify the method GET to list employees"""
        response = self.client.get('http://localhost:8000/employee/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_all(self):
        """Test POST to create an employee"""
        data = {
            'name': 'Jose Lima',
            'email': 'jose.lima@email.com.br',
            'department': 'rh'
        }
        response = self.client.post(
                                    'http://localhost:8000/employee/',
                                    data=data
                                    )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_del_all(self):
        """Test to verify the method DELETE"""
        response = self.client.delete('http://localhost:8000/employee/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_all(self):
        """Test to verify the method PUT"""
        data = {
            'name': 'Jose Lima',
            'email': 'jose.lima@email.com.br',
            'department': 'humanresources'
        }
        response = self.client.put(
                                    'http://localhost:8000/employee/2/',
                                    data=data
                                )
        self.assertEquals(response.status_code, status.HTTP_200_OK)
