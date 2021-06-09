from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.airports)
admin.site.register(models.flights)
admin.site.register(models.user_login)
admin.site.register(models.Departs)