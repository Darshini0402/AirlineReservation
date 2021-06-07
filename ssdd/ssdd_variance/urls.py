
from django.urls import path
from . import views

urlpatterns = [
    path('',views.search,name='searchflight'),
    path('Login.html', views.Login,name='Login'),
    path('Admin.html', views.Admin,name='Admin'),
    path('User.html', views.User,name='User'),
    path('firstpage.html', views.firstpage,name='firstpage'),
    path('sign.html', views.sign,name="sign"),
    path('faq.html', views.faq,name='faq'),
    path('bagsnmeals.html', views.bagsnmeals,name='bagsnmeals'),
    path('aboutus.html', views.aboutus,name='aboutus'),
]