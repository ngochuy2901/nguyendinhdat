
from django import template
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
# from django.template import loader
# Create your views here.
#hiển thị thông tin khách hàng
def displayCustomerInfo(request):
    user = User.objects.get(username='root')
    
    template = loader.get_template('profile.html')
    context = {
        'user': user,
    }
    # return HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))
    # return render(request=request, template_name='profile.html')

