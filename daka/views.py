from django.shortcuts import render, redirect
from django.db import models

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password :
            username = username.strip()
            try :
                user = models.User.object.get(name=username)
            except:
                return render(request ,'login',{'msg':'error'})
            if user.password == password:
                return render('index.html',{'hello':"hello"})
    return render(request, 'login.html', {})
