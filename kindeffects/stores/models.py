from django.db import models
from imagekit.models import ProcessedImageField
from django.core import serializers

# Create your models here.
# class StoreManager(models.Manager):
#     def get_by_natural_key(self, name, num, addr, open_hour, closed_hour, service):
#         return self.get(name=name, num=num, addr=addr, open_hour=open_hour, closed_hour=closed_hour, service=service)


class Store(models.Model):
    name = models.CharField(max_length=100)
    num = models.CharField(max_length=100)
    addr = models.CharField(max_length=500)
    open_hour = models.TimeField()
    closed_hour = models.TimeField()
    service = models.TextField()    

    # objects = StoreManager()

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name

    # class Meta:
    #     unique_together = [['name',]]


class Visiting(models.Model):
    visiting_time = models.DateTimeField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)


