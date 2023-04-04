from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from manager.departament.models import Departament


class AllTestCase(APITestCase):

    def setUp(self):
        user = User.objects.create(username='user')
        user.set_password('user')
        user.save()
        self.client.force_authenticate(user=user)
        self.list_url = 'http://localhost:8000/departament/'
        self.employee1 = Departament.objects.create(
                    name='Human Resources'
        )
        self.employee2 = Departament.objects.create(
                    name='Development'
                    )

    def test_get_all(self):
        """Test GET to verify the method GET to list departaments"""
        response = self.client.get('http://localhost:8000/departament/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_all(self):
        """Test POST to create an departament"""
        data = {
            'name': 'Infrastructure'
        }
        response = self.client.post(
                                    'http://localhost:8000/departament/',
                                    data=data
                                    )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_del_all(self):
        """Test to verify the method DELETE"""
        response = self.client.delete('http://localhost:8000/departament/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_all(self):
        """Test to verify the method PUT"""
        data = {
            'name': 'Infrastruture'
        }
        response = self.client.put(
                                    'http://localhost:8000/departament/2/',
                                    data=data
                                )
        self.assertEquals(response.status_code, status.HTTP_200_OK)
