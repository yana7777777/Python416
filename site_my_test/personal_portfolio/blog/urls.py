from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('<int:blog_id>/', views.detail, name="detail"),

        # Auth (регистрация и авторицзация) добавила 20.07.25
    path('signup', views.signup_user, name='signupuser'),
    path('logout/', views.logout_user, name='logoutuser'),
    path('login/', views.login_user, name='loginuser'),
]
