from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import *

import re

def index(request):
    all_user = User.objects.all()
    context = {
        'all_user' : all_user
    }
    return render(request, 'python_exam_app/index.html', context)

def create(request):
    new_user = User.objects.create(

        name = request.POST['name'], 
        username = request.POST['username'],
        password = request.POST['password'],
        confirm_pw = request.POST['confirm_pw'])

    return redirect('/dashboard')

def dashboard(request):
    
    all_trip = Trip.objects.all()
    context = {
        'all_trip' : all_trip
    }

    return render(request,'python_exam_app/dashboard.html', context)

def add(request):
     return render(request, 'python_exam_app/add.html')

def adddes(request):

    new_destination = Trip.objects.create(

    destination = request.POST['destination'],
    description = request.POST['description'],
    travel_start_date = request.POST['travelFrom'],
    travel_end_date = request.POST['travelTo'])

    print new_destination

    return redirect('/dashboard')

def show(request, id):
    context = {
        'trip' : Trip.objects.get(id = id)
    }
    return render(request, '/show.html',context)

def destroy(request, id):
    User.objects.filter(id = id).delete()
    return redirect('/')
    


