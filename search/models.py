from django.db import models

# Create your models here.
from django.conf import settings

class SearchQuery(models.Model):
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()