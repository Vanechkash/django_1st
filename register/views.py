from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    res = {'url':'login'}
    if request.GET:
        password = request.GET['password']
        user = request.GET['user']
        u = auth.authenticate(username=user, password=password)
        if u:
            auth.login(request, u)
            return redirect('/')
        else:
            res['error'] = 'wrong user or password'
            return render(request, 'register.html', res)
    else:
        return render(request, 'register.html', res)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    res = {'url':'register'}
    if request.GET:
        password = request.GET['password']
        user = request.GET['user']
        new_user = User.objects.create_user(username=user, password=password)
        auth.login(request, new_user)
        return redirect('/')
    else:
        return render(request, 'register.html', res)
# Create your views here.
