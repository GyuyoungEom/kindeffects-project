from django.db import models
from django.contrib.auth.models import AbstractUser
from stores.models import Store

class User(AbstractUser):
    phone = models.CharField(max_length=20)
    name_kr = models.CharField(max_length=10)
    store_regist = models.CharField(max_length=100)
    # store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)
    store = models.OneToOneField(Store, on_delete=models.CASCADE, blank=True, null=True)