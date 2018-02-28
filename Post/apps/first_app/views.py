from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from django.core import serializers
import json
def index(request):
    return render(request, 'user_login/index.html')

def all_html(request):
    notes = note.objects.all()
    return render(request, 'user_login/all.html', { "notes": notes })

def create(request):
    note.objects.create(message = request.POST['message'])
    notes = note.objects.all()
    return render(request, 'user_login/all.html',{ "notes": notes })