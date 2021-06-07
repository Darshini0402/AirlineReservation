from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class airports(models.Model):
    code=models.CharField(max_length=3, primary_key=True)
    airport_name=models.CharField(max_length=64)
    city=models.CharField(max_length=10)
    
    def __str__(self):
        return f" {self.city}"

class flights(models.Model):
    flightno=models.CharField(max_length=7,primary_key=True)
    origin=models.ForeignKey(airports,on_delete=models.CASCADE, related_name='departure')
    destination=models.ForeignKey(airports,on_delete=models.CASCADE, related_name='arrival')
    duration=models.IntegerField()
    business=models.IntegerField()
    economy=models.IntegerField()
    def __str__(self):
        return f" {self.flightno}"

class user_login(models.Model):
    name=models.CharField(max_length=64)
    mobile=models.IntegerField()
    email_id=models.CharField(max_length=64)
    username=models.CharField(max_length=20, primary_key=True)
    password=models.CharField(max_length=16)
    
    def __str__(self):
        return f" {self.user.username}"