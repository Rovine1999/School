from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect


# Create your views here.


def signup(request):
    return render(request, template_name='account/pages/signup.html', context={})


def account_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged In!')
            return redirect('home')
        else:
            messages.error(request, 'Login failed! Check your username and password.')
            return render(request, template_name='account/pages/login.html', context={'page': 'login'})
    return render(request, template_name='account/pages/login.html', context={})


def account_logout(request):
    logout(request)
    return redirect('home')
