from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from itertools import chain
from itertools import groupby
from models import *
from django.core import serializers
import json
def index(request):
    leads = Lead.objects.all()
    num =0
    if leads > 10:
        for count in range(0, len(leads)):
            num = num + 1
    return render(request, 'user_login/index.html', { "num": num })
# Create your views here.
def all_json(request):
    users = Lead.objects.all()
    users_json = serializers.serialize("json", users)
    return HttpResponse(users_json, content_type='application/json')
def all_html(request):
    users = Lead.objects.filter(id__range = (0, 10))
    return render(request, 'user_login/all.html', { "users": users })
def find(request):
    users = Lead.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])
    users2 = Lead.objects.filter(last_name__startswith=request.POST['first_name_starts_with'])
    user_list =  users | users2
    # list(chain(users, users2))
    # unique_results = [rows.next() for (key, rows) in groupby(result_list, key=lambda obj: obj.id)]
    return render(request, 'user_login/all.html', {"users": user_list})
def create(request):
    Lead.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'])
    users = Lead.objects.filter(id__range = (0, 10))
    return render(request, 'user_login/all.html',{ "users": users })

def date(request):
    user_list = Lead.objects.filter(created_at__range =(request.POST['date_start'],request.POST['date_end']))
    return render(request, 'user_login/all.html', {"users": user_list})

def ranges(request):
    nums = request.GET['page']
    nums = int(nums)
    nums = nums * 10
    numbers = nums - 9
    user_list = Lead.objects.filter(id__range = (numbers, nums))
    return render(request, 'user_login/all.html', {"users": user_list})