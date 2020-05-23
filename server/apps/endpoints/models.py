from django.db import models

# Create your models here.

class Endpoint(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    createdAt = models.DateTimeField(auto_now_add=True, blank=False)

