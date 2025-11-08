from django.db import models

# Create your models here.

class RegisterUser(models.Model):
    reg_mail=models.CharField(max_length=100,blank=False,unique=True)
    reg_password=models.CharField(max_length=100,blank=False)
