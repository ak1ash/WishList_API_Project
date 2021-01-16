from django.db import models
from django.db.models import Model
import uuid


# Create your models here.

class PrivateWish(models.Model):
    wish_id = models.AutoField(primary_key=True)
    wish = models.CharField(max_length=255, blank=False, default='')
    destination_uri = models.CharField(max_length=255, blank=False, default='')
    image_uri = models.CharField(max_length=255, blank=False, default='')
    amount_wished = models.CharField(max_length=255, blank=False, default='')

class PublicWish(models.Model):
    wish_id = models.AutoField(primary_key=True)
    wish = models.CharField(max_length=255, blank=False, default='')
    destination_uri = models.CharField(max_length=255, blank=False, default='')
    image_uri = models.CharField(max_length=255, blank=False, default='')
    amount_wished = models.CharField(max_length=255, blank=False, default='')
    amount_granted = models.CharField(max_length=255, blank=True, default='')

class AccessModel(models.Model):
    access_uuid = models.UUIDField(default = uuid.uuid4)
    access_level = models.CharField(max_length=10)


