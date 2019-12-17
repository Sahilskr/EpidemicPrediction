from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    helpno= models.CharField(max_length=255)
