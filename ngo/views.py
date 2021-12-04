from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    #ngos=NGO.objects.all()
    ngos = Organization.objects.raw('select * from ngo_organization')
    data={'ngos':ngos}
    print(data)
    return render(request, 'index.html',data)

def register_ngo(request):
    return render(request,'register_ngo.html')