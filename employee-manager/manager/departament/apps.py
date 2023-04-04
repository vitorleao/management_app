from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'compfactu.core'


class DepartamentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'departament'
