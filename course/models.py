from django.db import models

# Create your models here.
class Course(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=10)
    duration=models.CharField(max_length=30)
    details=models.TextField(max_length=200)
