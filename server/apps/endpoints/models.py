from django.db import models
'''
name: Name of the endpoint that will appear on the URL as {localhost}/api/v1/{name}/predict
owner: Name of the owner associated with the endpoint and model
createdAt: The date and time the endpoint was created at  
'''
class Endpoint(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    createdAt = models.DateTimeField(auto_now_add=True, blank=False)

'''
name: Name of the algorithm
description: Short description of the algorithm
code: The code of the algorithm in server/apps/ml/{name}.py file
version: Version of the algorithm
owner: Owner of the algorithm
createdAt: The date and time the model was created at 
parentEndpoint: The endpoint the model will be served at as represented by the Endpoint model above
'''
class MlAlgorithm(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    parentEndpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

'''
status: The status of the algorithm - production, staging, testing etc 
active: Boolean value representing whether the model is active or not
createdBy: The name of the creator of the status
createdAt: The time and date the status was created at 
parentAlgorithm: The algorithm this status refers to as represented by the MlAlgorithm model above 
'''
class MlAlgorithmStatus(models.Model):
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    createdBy = models.CharField(max_length=128)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    parentAlgorithm = models.ForeignKey(MlAlgorithm, on_delete=models.CASCADE, related_name="status")

'''
inputData: Raw input data associated with this request 
fullResponse: Full JSON response to the request 
response: Label given to this input by the model (considering there was no error)
createdAt: The date and time this request was created at 
parentAlgorithm: The model associated with this request as represented by the MlAlgorithm model above 
'''
class MLRequest(models.Model):
    inputData = models.CharField(max_length=10000)
    fullResponse = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    parentAlgorithm = models.ForeignKey(MlAlgorithm, on_delete=models.CASCADE)