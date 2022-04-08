from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def login(request):
    return render(request, 'main/login.html')

def shop(request):
    return render(request, 'main/shop.html')

def contactus(request):
    return render(request, 'main/contactus.html')

def liked(request):
    return render(request, 'main/liked.html')

def basket(request):
    return render(request, 'main/basket.html')