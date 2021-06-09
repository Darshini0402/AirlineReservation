
from django.urls import path
from . import views

from django.urls import path
from django.utils import html
from . import views

urlpatterns = [
    path('searchflight.html',views.search,name='searchflight'),
    path('firstpage.html', views.firstpage,name='firstpage'),
    path('Login.html', views.Login,name='Login'),
    path('sign.html',views.sign,name='sign'),
    path('Admin.html', views.Admin,name='Admin'),
    path('User.html', views.User,name='User'),
    path('faq.html', views.faq,name='faq'),
    path('bagsnmeals.html', views.bagsnmeals,name='bagsnmeals'),
    path('aboutus.html', views.aboutus,name='aboutus'),
]