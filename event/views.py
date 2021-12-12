from django.db import connection
from django.shortcuts import render, redirect
from django.contrib import messages
from event.models import Event
from ngo.models import Organization

cursor=connection.cursor()
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
    cred_points=int(request.POST['cred_points'])
    print(nid,ngo)
    #query='''INSERT INTO event_event (location,venue,ngo_id_id,name,description,cred_points) VALUES ('{}','{}','{}','{}','{}','{}');'''.format(location,venue,ngo,name,description,cred_points)
    #cursor.execute(query)
    events = Event.objects.create(location=location,venue=venue,ngo_id=ngo,name=name,description=description,cred_points=cred_points)
    events.save()
    return redirect('/ngo/{}'.format(nid))

def event_details(request,eid):
    eve_data=Event.objects.raw('''SELECT * FROM event_event WHERE id={};'''.format(eid))
    data={'eve_data':eve_data[0]}
    return render(request,'event_detail.html',data)