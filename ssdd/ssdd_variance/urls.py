
from django.urls import path
from . import views
from django.utils import html


urlpatterns = [
    path('',views.list,name="list"),
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('searchflight.html',views.search,name='searchflight'),
    path('firstpage.html', views.firstpage,name='firstpage'),
    path('sign.html',views.sign,name='sign'),
    path('User.html', views.User,name='User'),
    path('faq.html', views.faq,name='faq'),
    path('bagsnmeals.html', views.bagsnmeals,name='bagsnmeals'),
    path('aboutus.html', views.aboutus,name='aboutus'),
]