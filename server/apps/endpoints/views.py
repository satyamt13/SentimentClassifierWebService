from django.db import transaction
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from apps.endpoints.models import Endpoint
from apps.endpoints.serializers import EndpointSerializer
from apps.endpoints.models import MlAlgorithm
from apps.endpoints.serializers import MlAlgorithmSerializer
from apps.endpoints.models import MlAlgorithmStatus
from apps.endpoints.serializers import MlAlgorithmStatusSerializer
from apps.endpoints.models import MLRequest
from apps.endpoints.serializers import MLRequestSerializer
from rest_framework.exceptions import APIException
import json
from numpy.random import rand
from rest_framework import views, status
from rest_framework.response import Response
from apps.ml.registry import MlRegistry
from server.wsgi import registry
'''
View Objects associated with each of our models that will help us retrieve 
our model objects as we need them as well as well as directly supply input 
and get a prediction using the GUI on the /api/v1/{model}/predict page 
in addition to being able to make http calls to the REST API 
'''
class EndpointViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()

class MlAlgorithmViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MlAlgorithmSerializer
    queryset = MlAlgorithm.objects.all()

def deactivate_other_statuses(instance):
    old_statuses = MlAlgorithmStatus.objects.filter( parentAlgorithm = instance.parentAlgorithm,
                                                     createdAt = instance.createdAt,
                                                     active = True)
    for i in range( len(old_statuses) ):
        old_statuses[i].active = False
    MlAlgorithmStatus.objects.bulk_update(old_statuses, ["active"])

class MlAlgorithmStatusViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.CreateModelMixin
):
    serializer_class = MlAlgorithmStatusSerializer
    queryset = MlAlgorithmStatus.objects.all()
    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                deactivate_other_statuses(instance)
        except Exception as e:
            raise APIException(str(e))

class MLRequestViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.UpdateModelMixin
):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()

class PredictView(views.APIView):
    def post(self, request, endpoint_name, format=None):
        algorithm_status = self.request.query_params.get("status", "production")
        algorithm_version = self.request.query_params.get("version")
        algs = MlAlgorithm.objects.filter(parentEndpoint__name=endpoint_name, status__status=algorithm_status,
                                          status__active=True)
        if algorithm_version is not None:
            algs = algs.filter(version=algorithm_version)
        if len(algs) == 0:
            return Response(
                {"status": "Error", "message": "Ml algorithm is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if len(algs) == 500:
            print(algs)
            return Response(
                {"status": "Error", "message": "Ml Algorithm selection is ambiguous. Please specify algorithm version"},
                status=status.HTTP_400_BAD_REQUEST
            )
        alg_index = 0
        algorithm_object = registry.endpoints[algs[alg_index].id] #registry.endpoints[10]
        prediction = algorithm_object.compute_prediction(request.data)
        label = prediction["Label"] if "Label" in prediction else "error"
        ml_request = MLRequest(
            inputData=json.dumps(request.data),
            fullResponse=prediction,
            response=label,
            feedback="",
            parentAlgorithm=algs[alg_index],
        )
        ml_request.save()
        prediction["request_id"] = ml_request.id
        return Response(prediction)












