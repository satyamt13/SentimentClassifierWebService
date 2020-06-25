from django.contrib import admin
from apps.endpoints.models import Endpoint
from apps.endpoints.models import MlAlgorithm
from apps.endpoints.models import MlAlgorithmStatus
from apps.endpoints.models import MLRequest
# Register your models here.
admin.site.register(Endpoint)
admin.site.register(MlAlgorithm)
admin.site.register(MlAlgorithmStatus)
admin.site.register(MLRequest)

