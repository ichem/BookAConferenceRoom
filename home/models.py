from django.db import models

class Rooms(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=64)
    description = models.DateField()