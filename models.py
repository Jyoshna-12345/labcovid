from django.db import models
from django.forms import ModelForm
# Create your models here.
class Login(models.Model):
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=10)
