from django.http import response
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
def index(request):
    #ngos=NGO.objects.all()
    ngos = Organization.objects.raw('select * from ngo_organization')
    data={'ngos':ngos}
    return render(request, 'index.html',data)

@csrf_exempt
def register_ngo(request):
    if request.method == "POST":
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        location=request.POST['location']
        phone=request.POST['phone']
        description=request.POST['description']
        links=request.POST['links']
        logo=request.FILES['logo']
        if password==confirm_password:
            if Organization.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('Register')
            elif Organization.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('Register')
            else:
                user=Organization.objects.create_user(username=username,password=password,email=email,name=name,location=location,phone=phone,description=description,links=links,logo=logo)
                user.save()
                messages.info(request,'Success')
                return JsonResponse({'Login':'successfull'})
        else:
            messages.info(request,'Password does not match')
            return redirect('Register')
    return render(request,'register_ngo.html')