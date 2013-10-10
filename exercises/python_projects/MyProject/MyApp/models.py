from django.db import models

class Player(models.Model):
    name = models.CharField(max_length= 20)
    joined = models.DateField()
# Create your models here.
