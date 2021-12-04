from django.db import models
from ngo.models import Organization

# Create your models here.
class Event(models.Model):
    location=models.TextField()
    venue=models.TextField()
    ngo_id=models.ForeignKey(Organization,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name