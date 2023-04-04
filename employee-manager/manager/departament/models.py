from django.db import models
from django.utils.translation import gettext as _


class Departament(models.Model):
    name = models.CharField(_("name"), max_length=255)
