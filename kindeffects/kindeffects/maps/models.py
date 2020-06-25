from django.db import models
from stores.models import Store

# Create your models here.
class Map(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    store = models.ForeignKey(Store,on_delete=models.CASCADE)