from django.db import models

# Create your models here.

class Profile(models.Model):
    username=models.CharField( max_length=100,default="")
    fname=models.CharField( max_length=50)
    sname=models.CharField( max_length=50)
    email=models.EmailField( max_length=254,unique=True)
    password=models.CharField( max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.CharField(default="", max_length=50)

    def __str__(self):
        return self.fname+" "+self.sname

 