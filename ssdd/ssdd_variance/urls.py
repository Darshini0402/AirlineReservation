
from django.urls import path
from . import views

from django.urls import path
from django.utils import html
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.Login,name='Login'),
    path('searchflight.html',views.search,name='searchflight'),
=======
    path('searchflight.html',views.search,name='searchflight'),
    path('firstpage.html', views.firstpage,name='firstpage'),
    path('Login.html', views.Login,name='Login'),
    path('sign.html',views.sign,name='sign'),
>>>>>>> e22d096d62608e708df0ccda57566c6eb5a58acc
    path('Admin.html', views.Admin,name='Admin'),
    path('User.html', views.User,name='User'),
    path('faq.html', views.faq,name='faq'),
    path('bagsnmeals.html', views.bagsnmeals,name='bagsnmeals'),
    path('aboutus.html', views.aboutus,name='aboutus'),
]