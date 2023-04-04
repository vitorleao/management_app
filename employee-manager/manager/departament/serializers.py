from rest_framework import serializers
from manager.departament.models import Departament


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = ['name']
