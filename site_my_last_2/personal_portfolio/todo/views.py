from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from todo import views


def current_todos(request):
    todos = Todo.objects.order_by('-created')
    return render(request, 'todo/currenttodos.html', {"todos": todos})


def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todo/tododetails.html', {'todo': todo})

