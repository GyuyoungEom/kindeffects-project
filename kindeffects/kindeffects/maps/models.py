from django.db import models
from stores.models import Store

# Create your models here.

class Code(models.Model):
    si = models.CharField(max_length=200)
    code = models.IntegerField()
    def __str__(self):
        return self.si

class Map(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    # dong = models.CharField(max_length=200)
    store = models.OneToOneField(Store,on_delete=models.CASCADE)
    # code = models.one(Code,on_delete=models.CASCADE)