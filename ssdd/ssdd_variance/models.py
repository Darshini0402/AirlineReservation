from django.db import models
class Destination(models.Model):
    name =models.CharField(max_length=100)
    
    desc=models.TextField()
    price=models.IntegerField
    offer=models.BooleanField(default=False)

# Create your models here.
