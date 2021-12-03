from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    #ngos=NGO.objects.all()
    ngos = NGO.objects.raw('select * from NGO')
    data={'ngos':ngos}
    print(data)
    return render(request, 'index.html',data)