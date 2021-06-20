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


class Departs(models.Model):
    sno=models.IntegerField(primary_key=True)
    flight_no=models.ForeignKey(flights,on_delete=models.CASCADE, related_name='flight_code')
    dep=models.ForeignKey(airports,on_delete=models.CASCADE, related_name='origin_code')
    arr=models.ForeignKey(airports,on_delete=models.CASCADE, related_name='destination_code')
    departure_time=models.CharField(max_length=64)
    arrival_time=models.CharField(max_length=64)
    
class user_login(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE, related_name="uname")
    first_name=models.OneToOneField(User,on_delete=models.CASCADE, related_name="fname")
    last_name=models.OneToOneField(User,on_delete=models.CASCADE, related_name="lname")
    email=models.OneToOneField(User,on_delete=models.CASCADE, related_name="mail")
    password=models.OneToOneField(User,on_delete=models.CASCADE, related_name="passw")
    
    def __str__(self):
        return f" {self.user.username}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    adhaar_no=models.CharField(max_length=20, primary_key=True)
    phone_no=models.CharField(max_length=64)
    def __str__(self):
        return f" {self.first}"
          