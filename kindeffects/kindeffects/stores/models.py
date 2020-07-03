from django.db import models
from imagekit.models import ProcessedImageField

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    num = models.CharField(max_length=100)
    addr = models.CharField(max_length=500)
    open_hour = models.TimeField()
    closed_hour = models.TimeField()
    service = models.TextField()    

    def __str__(self):
        return self.name


class Visiting(models.Model):
    visiting_time = models.DateTimeField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)

