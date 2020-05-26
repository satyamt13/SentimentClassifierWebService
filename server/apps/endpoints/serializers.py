from rest_framework import serializers
from apps.endpoints.models import Endpoint
from apps.endpoints.models import MlAlgorithm
from apps.endpoints.models import MlAlgorithmStatus
from apps.endpoints.models import MLRequest

class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        read_only_fields = ("id","name","owner","createdAt")
        fields = read_only_fields

class MlAlgorithmSerializer(serializers.ModelSerializer):

    currentStatus = serializers.SerializerMethodField(read_only=True)

    def getCurrentStatus(self, MlAlgorithm):
        return MlAlgorithmStatus.objects.filter(parentAlgorithm = MlAlgorithm)\
    .latest("createdAt").status

    class Meta:
        model = MlAlgorithm
        read_only_fields = ("id", "name", "description", "code",
                            "version", "owner", "createdAt", "parentEndpoint",
                            "currentStatus")
        fields = read_only_fields

class MlAlgorithmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MlAlgorithmStatus
        read_only_fields = ("id", "active")
        fields = ("id", "active", "status", "createdBy",
                  "createdAt", "parentAlgorithm")

class MLRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLRequest
        read_only_fields = ("id", "inputData", "fullResponse","response",
                            "createdAt", "parentAlgorithm")
        fields = ("id", "inputData", "fullResponse", "response", "feedback",
                  "createdAt", "parentAlgorithm")



