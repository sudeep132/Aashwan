from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from volunteer.models import Volunteers
from django.db import connection
from event.models import Event
from django.contrib import messages

# Create your views here.
cursor=connection.cursor()
@csrf_exempt
def create_volunteer(request):
    if(request.method=="POST"):
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        email_id=request.POST['email']
        phone_no=request.POST['phone']
        gender=request.POST['gender']
        if(password==confirm_password):
            event_id=Event.objects.get(pk=1)
            query='''INSERT INTO volunteer_volunteers (password,username,name,email_id,phone_no,gender,event_id_id,credit) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');'''.format(password,username,name,email_id,phone_no,gender,1,0)
            cursor.execute(query)
            #volunteer=Volunteers.objects.raw('''INSERT INTO volunteer_volunteers (name,email_id,phone_no,gender,event_id_id,credit) VALUES ('{}','{}','{}','{}','{}','{}');'''.format(name,email_id,phone_no,gender,0,0))
            return redirect('/')
        else:
            messages.info(request,'Failed')
            return redirect('/')

def enroll_volunteer(request,eid):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        query='''SELECT password FROM volunteer_volunteers WHERE username='{}';'''.format(username)
        cursor.execute(query)
        data=cursor.fetchall()
        print(data[0][0])
        if data[0][0]==password:
            query='''UPDATE volunteer_volunteers SET event_id_id={} WHERE username='{}';'''.format(eid,username)
            cursor.execute(query)
            print("Hi")
            return redirect('/')
        messages.info(request,"Failed")
        return redirect('/')