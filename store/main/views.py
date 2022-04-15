from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login, logout




def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        sname = request.POST['sname']
        dateofbrth = request.POST['dateofbrth']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')

        myuser = User.objects.create_user(username, email, fname, sname, dateofbrth, pass1)
        myuser.is_active = False
        myuser.save()

        messages.success(request,
                         "Your Account has been created succesfully!")
    return render(request, 'main/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, "authentication/index.html")
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    return render(request, 'main/login.html')

def shop(request):
    return render(request, 'main/shop.html')

def contactus(request):
    return render(request, 'main/contactus.html')

def liked(request):
    return render(request, 'main/liked.html')

def basket(request):
    return render(request, 'main/basket.html')