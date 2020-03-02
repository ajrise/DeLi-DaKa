from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=11,unique=True)
    password = models.CharField(max_length=20)
    c_time = models.DateTimeField(auto_now_add=True)
    uuid = models.CharField(max_length=30,unique=True)