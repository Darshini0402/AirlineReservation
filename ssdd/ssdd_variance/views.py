from django.db.models.fields import CommaSeparatedIntegerField
from django.http import request
from django.http.request import validate_host
from django.utils.regex_helper import Choice
from .models import airports, flights, Departs, user_login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db.models.query import RawQuerySet
from django.db import connection
from datetime import date

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
        global n
        n = request.POST.get('count')
        global sh
        sh = request.POST.get('deptdate')
    return render(request,'searchflight.html',{
        "departs": Departs.objects.all(),"from":fcity,"to":tcity, "fl":flights.objects.all(),
    })

def bagsnmeals(request):
    if request.method=='POST':
        global f,l
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        global a
        a=request.POST.get('aadhar')
        p=request.POST.get('phone')
        cursor=connection.cursor()
        cursor.execute('INSERT INTO ssdd_variance_passenger (first,last,adhaar_no,phone_no) VALUES (%s,%s,%s,%s)',[f,l,a,p])
        connection.commit()
        connection.close()  
    return render(request,'bagsnmeals.html')

def passenger(request):    
    if request.method=='POST':
        global cost
        cost = request.POST.get('cl')
        slno = request.POST.get('choice')
        slno=int(slno)
        cursor=connection.cursor()
        cursor.execute("SELECT arrival_time, departure_time, flight_no_id FROM ssdd_variance_departs WHERE sno LIKE %s",(slno,))
        result = cursor.fetchall()
        global flight
        flight=result[0][2]
        global arr
        arr = result[0][0]
        global dep
        dep = result[0][1] 
        connection.commit()
        connection.close()  
    return render(request,'passenger.html',{"count":n})

def transaction(request):
    if request.method=='POST':
        i=request.POST.get('idli')
        c=request.POST.get('chinese')
        it=request.POST.get('italian')
        t=request.POST.get('thaali')
        m=request.POST.get('mocktail')
        p=request.POST.get('pizza')
    total=(int(cost))*(int(n))
    tma=int(i)*400+int(c)*300+int(m)*120+int(t)*420+int(it)*500+int(p)*800
    global totcost
    totcost = total+tma
    cursor=connection.cursor()
    #cursor.execute("CREATE SEQUENCE ticketno INCREMENT BY 1 START WITH 602021101 MINVALUE 602021101 MAXVALUE 6000000000 CYCLE CACHE 20;")
    cursor.execute("INSERT INTO ssdd_variance_ticket VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",[1,111,f,flight,arr,dep,sh,totcost])
    connection.commit()
    connection.close()
    return render(request,'transaction.html',{"amt":total, "meal_price":tma, 
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
    return render(request,'sign.html')   

def faq(request):
    return render(request,'faq.html')
def aboutus(request):
    return render(request,'aboutus.html')
def Login(request):
    return render(request,'Login.html')
def User(request):
    return render(request,'User.html')
def ticket(request):
    return render(request,'ticket.html',{"date":sh,"cost":totcost,"flight":flight,"arr":arr,"dep":dep})


