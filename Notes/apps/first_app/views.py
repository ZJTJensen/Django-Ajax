from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from django.core import serializers
import json
def index(request):
    return render(request, 'user_login/index.html')
# Create your views here.
def all_html(request):
    users = User.objects.all()
    return render(request, 'user_login/all.html', { "users": users })
def create(request):
    User.objects.create(name=request.POST['name'], message=request.POST['message'])
    users = User.objects.all()
    return render(request, 'user_login/all.html',{ "users": users })
def edit(request, id):
    this_user = User.objects.get(id=id)
    this_user.message= request.POST['message']
    this_user.save() 
    users = User.objects.all()
    return render(request, 'user_login/all.html',{ "users": users })
def delete(request, id):
    usery = User.objects.get(id=id)
    usery.delete()
    users = User.objects.all()
    return render(request, 'user_login/all.html',{ "users": users })