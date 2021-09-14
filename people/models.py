from django.db import models
from django.db.models.base import Model

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length= 20)
    age = models.IntegerField()
    dateOfBirth = models.DateField()

    def __str__(self):
        return self.name
