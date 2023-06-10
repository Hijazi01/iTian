from django.db import models

import course.models
from course.models import *
#Create your models here.
class Mytrainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.CharField(max_length=3)
    email=models.EmailField(unique=True)
    faculty= models.TextField(max_length=50)
    appreciation=models.CharField(max_length=12)
    # idcourses=models.ForeignKey('course.Course',on_delete=models.CASCADE)
