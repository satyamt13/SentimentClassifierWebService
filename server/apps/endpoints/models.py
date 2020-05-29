from django.db import models

# Create your models here.

class Endpoint(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    createdAt = models.DateTimeField(auto_now_add=True, blank=False)

class MlAlgorithm(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    parentEndpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

class MlAlgorithmStatus(models.Model):
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    createdBy = models.CharField(max_length=128)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    parentAlgorithm = models.ForeignKey(MlAlgorithm, on_delete=models.CASCADE)

class MLRequest(models.Model):
    inputData = models.CharField(max_length=10000)
    fullResponse = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    parentAlgorithm = models.ForeignKey(MlAlgorithm, on_delete=models.CASCADE)









