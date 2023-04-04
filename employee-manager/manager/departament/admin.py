from django.contrib import admin
from manager.departament.models import Departament


class Departaments(admin.ModelAdmin):
    list_display = (
                    'id',
                    'name'
                    )
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Departament, Departaments)
