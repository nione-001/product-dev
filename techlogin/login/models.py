from django.db import models

class Account(models.Model):
    email = models.CharField(max_length=30)
    passw = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

class ForgetPass(models.Model):
    email = models.CharField(max_length=30)
    rlink = models.CharField(max_length=30,default="hello")