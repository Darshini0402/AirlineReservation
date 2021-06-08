from .models import airports, flights, user_login
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def firstpage(request):
    answer = request.POST.get('fromcity')
    
    return render(request,'firstpage.html',{
        "cities": airports.objects.all(), "choice": answer
    })

"""class fromcity(CreateView):
    model = airports
    form_class = PersonForm
    success_url = reverse_lazy('firstpage')

class tocity(UpdateView):
    model = airports
    form_class = PersonForm
    success_url = reverse_lazy('firstpage')
def load_cities(request):
    country_id = request.GET.get('from')
    city = airports.objects.filter(country_id=country_id).order_by('city')
    return render(request, 'firstpage.html', {'cities': city})"""


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


