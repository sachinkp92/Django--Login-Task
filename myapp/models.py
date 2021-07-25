from django.db import models

# Create your models here.
class BasicDetails(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    mothername=models.CharField(max_length=100)
    dateofbirth=models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    about=models.TextField(max_length=200)

class Education(models.Model):
    coursename=models.CharField(max_length=100)
    universityname=models.CharField(max_length=100)
    passingyear=models.CharField(max_length=100)

