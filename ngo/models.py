from django.db import models

# Create your models here.
class NGO(models.Model):
    location=models.TextField()
    links=models.TextField()
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="images")
    helpline_no=models.CharField(max_length=30)
    description=models.TextField()

class Events(models.Model):
    location=models.TextField()
    venue=models.TextField()
    ngo_id=models.ForeignKey(NGO,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=100)
    description=models.TextField()