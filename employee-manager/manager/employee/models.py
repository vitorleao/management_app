from django.db import models
from django.utils.translation import gettext as _


class Employee(models.Model):
    name = models.CharField(_("name"), max_length=255)
    email = models.EmailField(_("email"), max_length=255)
    department = models.CharField(_("department"), max_length=255)
