from django.contrib import admin
from manager.employee.models import Employee


class Employees(admin.ModelAdmin):
    list_display = (
                    'id',
                    'name',
                    'email',
                    'department'
                    )
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Employee, Employees)
