from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('shop', views.shop, name='shop'),
    path('contactus', views.contactus, name='contactus'),
    path('liked', views.liked, name='liked'),
    path('basket', views.basket, name='basket'),
]
