from django.db import models
from event.models import Event

# Create your models here.
class Volunteers(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField(max_length=100)
    phone_no=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    credit=models.IntegerField(default=0)
    event_id=models.ForeignKey(Event,on_delete=models.CASCADE,default=None,null=True)

    def __str__(self):
        return self.name