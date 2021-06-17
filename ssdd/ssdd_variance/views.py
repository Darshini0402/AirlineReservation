from .models import airports, flights, user_login, Departs
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def firstpage(request):
    if request.method == 'POST':
        fcity = request.POST.get('fromcities')
    return render(request,'firstpage.html',{
        "cities": airports.objects.all(), "from":fcity
    })

def searchflight(request):
    if request.method == 'POST':
        fcity = request.POST.get('fromcities')
        tcity = request.POST.get('tocities')
    return render(request,'searchflight.html',{
        "departs": Departs.objects.all(),"from":fcity,"to":tcity, "fl":flights.objects.all()
    })

def list(request):
    return render(request,'firstpage.html',{
        "cities": airports.objects.all(), 
    })

def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    #return render(request,"firstpage.html")
def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]
        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
            # Otherwise, return login page again with new context
        else:
            return render(request, "login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "login.html")
def logout_view(request):
    logout(request)
    return render(request, "login.html", {
                "message": "Logged Out"
            })
    


def sign(request):
    if request.method == 'POST':
        if request.POST.get('Password') == request.POST.get('Repassword'):
            #if request.POST.get('Username') not in list(user_login.objects.select('username')):
                u=user_login()
                u.name= request.POST.get('Name')
                u.mobile= request.POST.get('Mobile')
                u.email_id= request.POST.get('Email')
                u.username= request.POST.get('Username')
                u.password= request.POST.get('Password')
                u.save()
                return render(request, 'Login.html')  
        else:
            print("invalid")
    else:
        return render(request,'sign.html')
    return render(request,'sign.html')

def bagsnmeals(request):
    return render(request,'bagsnmeals.html')
def faq(request):
    return render(request,'faq.html')
def aboutus(request):
    return render(request,'aboutus.html')

def Login(request):
    return render(request,'Login.html')
def User(request):
    return render(request,'User.html')


