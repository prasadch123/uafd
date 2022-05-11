from django.db import models
from django.contrib.auth.models import User
class Register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    aadhar=models.CharField(max_length=100)
    userid=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)

    def __str__(self):
        return self.user.username