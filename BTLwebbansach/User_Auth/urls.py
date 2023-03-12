from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginForm, name='login'),
    path('register', views.registerForm, name='register'),
    path('registerUser', views.registerUser),
    path('login', views.doLogin),
    path('forgotPassword', views.forgotPassword)
]
