
from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstpage,name='firstpage'),
    path('sign.html', views.sign,name="sign"),
    path('faq.html', views.faq,name='faq'),
    path('bagsnmeals.html', views.bagsnmeals,name='bagsnmeals'),
    path('aboutus.html', views.aboutus,name='aboutus'),
]