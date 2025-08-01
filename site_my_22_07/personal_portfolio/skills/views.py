from django.shortcuts import render, redirect
from .models import Skills
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Ability


def signup_user(request):
    if request.method == "GET":
        return render(request, 'skills/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'skills/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'Такое имя пользователя уже существует, задайте другое'})
        else:
            return render(request, 'skills/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def index(request):
    projects = Skills.objects.all()
    return render(request, 'skills/index.html', {'projects': projects})


def ability(request):
    projects = Skills.objects.all()
    return render(request, 'skills/ability.html', {'projects': projects})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')


def login_user(request):
    if request.method == "GET":
        return render(request, 'skills/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'skills/loginuser.html', {'form': AuthenticationForm(), 'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')


