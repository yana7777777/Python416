from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


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


def blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, "blog/blogs.html", {"blogs": blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


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

