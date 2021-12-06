from django.shortcuts import redirect, render

from volunteer.models import Volunteers

# Create your views here.
def create_volunteer(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email_id=request.POST['email']
        phone_no=request.POST['phone']
        gender=request.POST['gender']
        volunteer=Volunteers.objects.raw('''INSERT INTO volunteer_volunteers (name,email_id,phone_no,gender) VALUES ('{}','{}','{}','{}');'''.format(name,email_id,phone_no,gender))
        return redirect('/')