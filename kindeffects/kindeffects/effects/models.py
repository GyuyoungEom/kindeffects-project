from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    num = models.CharField(max_length=100)
    addr = models.CharField(max_length=1000)
    open_hour = models.TimeField()
    closed_hour = models.TimeField()
    service = models.TextField()


# class Partner(models.Model) :
#     account = models.CharField(max_length=100)
#     pwd = models.CharField(max_length=100)
#     hp = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
    

class Map(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    store = models.ForeignKey(Store,on_delete=models.CASCADE)