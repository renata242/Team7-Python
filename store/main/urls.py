from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('login', views.login),
    path('shop', views.shop),
    path('contactus', views.contactus),
    path('liked', views.liked),
    path('basket', views.basket),
]
