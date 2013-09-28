from django.db import models
from django.forms import ModelForm

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    school = models.CharField(max_length=255)