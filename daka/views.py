from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, reverse
from daka import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', {})
        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


def daka(request):
    if request.user.is_authenticated:
        user_uuid = request.user.myuser.uuid
        return render(request, 'daka.html', {'msg': user_uuid})
    else:
        return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
