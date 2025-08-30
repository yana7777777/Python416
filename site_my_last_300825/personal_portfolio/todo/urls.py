from django.urls import path
from . import views


urlpatterns = [
    path('', views.current_todos, name="todos"),
    path('<int:todo_id>/', views.todo_detail, name="tododetail"),

]

