from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Myuser(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)
    uuid = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return '{}'.format(self.username) 