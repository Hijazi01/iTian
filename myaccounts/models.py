from django.db import models

# Create your models here.
class MyUser(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=12)
    email=models.EmailField(unique=True)


