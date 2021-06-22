from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.airports)
admin.site.register(models.flights)
admin.site.register(models.user_login)
admin.site.register(models.Departs)
admin.site.register(models.Passenger)
<<<<<<< HEAD
admin.site.register(models.ticket)
=======
admin.site.register(models.ticket)
>>>>>>> 7ba833717887c7a3a2d1b4e8ac6885122ea0e4b5
