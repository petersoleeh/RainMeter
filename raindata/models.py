from django.db import models
from datetime import datetime
from django.shortcuts import render_to_response


# Create your models here.

class Raindata(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    month = models.CharField(max_length=20, unique=True)
    rainfall = models.IntegerField(default=0) #rainfall in MM

    def __str__(self):
        return self.month
