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
# Create your views here.
from rest_framework.exceptions import APIException


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
    MlAlgorithmStatus.objects.bulk_update( old_statuses, ["active"] )

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







