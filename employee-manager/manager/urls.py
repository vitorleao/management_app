from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from manager.departament.views import DepartamentViewSet, Departament
from manager.employee.views import EmployeeViewSet, Employee


router = routers.DefaultRouter()
router.register('departament', DepartamentViewSet, basename='departament')
router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('manager/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', include(router.urls)),
    path('departament-alphabetic/', Departament.as_view()),
    path('employee-alphabetic/', Employee.as_view()),
]
