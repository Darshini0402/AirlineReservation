from .models import flights
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstpage(request):
    return render(request,'firstpage.html')
def sign(request):
    return render(request,'sign.html')
def bagsnmeals(request):
    return render(request,'bagsnmeals.html')
def faq(request):
    return render(request,'faq.html')
def aboutus(request):
    return render(request,'aboutus.html')
def Admin(request):
    return render(request,'Admin.html')
def Login(request):
    return render(request,'Login.html')
def User(request):
    return render(request,'User.html')
def search(request):
    return render(request,'searchflight.html',{
        "flights" : flights.objects.all()
    })