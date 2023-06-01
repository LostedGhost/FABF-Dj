MAX_LENGHT_CHARFIELD = 30
MAX_LENGHT_DESCRIPTION = 255

from django.db import models

# Create your models here.

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=MAX_LENGHT_CHARFIELD)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    lastName = models.CharField(max_length=MAX_LENGHT_CHARFIELD)
    firstName = models.CharField(max_length=MAX_LENGHT_CHARFIELD)
    birthPlace = models.CharField(max_length=MAX_LENGHT_CHARFIELD)
    birthDate = models.DateField(auto_now=True)
    email = models.EmailField()
    userName = models.CharField(max_length=MAX_LENGHT_CHARFIELD)
    phone = models.CharField(max_length=MAX_LENGHT_CHARFIELD)
    password = models.CharField(max_length=MAX_LENGHT_CHARFIELD)
    gender = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=MAX_LENGHT_CHARFIELD)
    label = models.CharField(max_length=MAX_LENGHT_DESCRIPTION)
    link = models.CharField(max_length=MAX_LENGHT_CHARFIELD)