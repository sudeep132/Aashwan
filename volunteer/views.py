from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from volunteer.models import Volunteers
from django.db import connection
from event.models import Event

# Create your views here.
cursor=connection.cursor()
@csrf_exempt
def create_volunteer(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email_id=request.POST['email']
        phone_no=request.POST['phone']
        gender=request.POST['gender']
        event_id=Event.objects.get(pk=1)
        print(event_id)
        query='''INSERT INTO volunteer_volunteers (name,email_id,phone_no,gender,event_id_id,credit) VALUES ('{}','{}','{}','{}','{}','{}');'''.format(name,email_id,phone_no,gender,1,0)
        cursor.execute(query)
        #volunteer=Volunteers.objects.raw('''INSERT INTO volunteer_volunteers (name,email_id,phone_no,gender,event_id_id,credit) VALUES ('{}','{}','{}','{}','{}','{}');'''.format(name,email_id,phone_no,gender,0,0))
        return redirect('/')