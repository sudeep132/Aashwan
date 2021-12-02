from django.db import models
from ngo.models import Events

# Create your models here.
class Volunteers(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.EmailField(max_length=100)
    phone_no=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    event_id=models.ForeignKey(Events,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name