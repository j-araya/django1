from django.db import models

# Create your models here.

class Productos(models.Model):

    name = models.CharField(max_length=30)
    image = models.ImageField()
    price = models.IntegerField()
    date = models.DateField()
    usado = models.BooleanField()
