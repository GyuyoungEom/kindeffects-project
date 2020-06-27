from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    num = models.CharField(max_length=100)
    addr = models.CharField(max_length=500)
    open_hour = models.TimeField()
    closed_hour = models.TimeField()
    service = models.TextField()    