from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import Lower

from manager.departament.models import Departament
from manager.departament.serializers import DepartamentSerializer


class DepartamentViewSet(viewsets.ModelViewSet):
    """Lists all departaments ordered by id"""
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
    http_method_names = ['get', 'post', 'put', 'path', 'delete']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class Departament(generics.ListAPIView):
    """Lists all departaments ordered by name"""
    queryset = Departament.objects.all().order_by(Lower("name"))
    serializer_class = DepartamentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
