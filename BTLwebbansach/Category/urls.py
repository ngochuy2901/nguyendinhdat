from django.urls import path
from . import views

urlpatterns = [
    # path('', views.displayCustomerInfo, name='DisplayCustomerInfo'),
    path('home', views.home, name='home')
]
