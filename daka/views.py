from django.shortcuts import render, redirect,HttpResponseRedirect
from . import models

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def login(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        message = "所有字段都必须填写"
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return render(request,'index.html',{'hello':"正确"+user.name+':'+user.password+"输入:"+username+":"+password,'msg':message})    
                else:
                    message = "密码不正确"
            except:
                message = "用户不存在"

        return render(request,'index.html',{'hello':'错误'+user.name+':'+user.password+"输入:"+username+":"+password,'msg':message})
    return render(request, 'login.html', {})
