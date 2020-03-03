from django.shortcuts import render, redirect, HttpResponseRedirect , HttpResponse ,reverse
from . import models
from django.contrib.auth import authenticate, login, logout

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
            return render(request, 'index.html', {'hello': "验证通过"})
        else:
            return render(request, 'login.html', {'hello': "用户名或密码错误"})
    else:
        return render(request, 'login.html', {})


def daka(request):
    if request.user.is_authenticated:
        return render(request, 'daka.html', {'msg': "登录成功"})
    else:
        return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
