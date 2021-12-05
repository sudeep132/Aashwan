from django.shortcuts import render, redirect
from django.contrib import messages
from event.models import Event
from ngo.models import Organization

# Create your views here.
def create_event(request,nid):
    if nid!=request.user.id or request.method!="POST":
        print(nid,request.user.id)
        messages.info(request,'You are not authorized to create an event')
        return redirect('/')
    location=request.POST['location']
    venue=request.POST['venue']
    name=request.POST['name']
    description=request.POST['description']
    ngo=Organization.objects.get(pk=nid)
    events = Event.objects.create(location=location,venue=venue,ngo_id=ngo,name=name,description=description)
    events.save()
    return redirect('/ngo/{}'.format(nid))