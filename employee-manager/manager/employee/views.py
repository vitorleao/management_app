from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import Lower

from manager.employee.models import Employee
from manager.employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """Lists all employees ordered by id"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'put', 'path', 'delete']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class Employee(generics.ListAPIView):
    """Lists all employees ordered by name"""
    queryset = Employee.objects.all().order_by(Lower("name"))
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
