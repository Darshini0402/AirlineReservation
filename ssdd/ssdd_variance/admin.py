from django.contrib import admin
from .import models
admin.site.register(models.airports)
admin.site.register(models.flights)
# Register your models here.
