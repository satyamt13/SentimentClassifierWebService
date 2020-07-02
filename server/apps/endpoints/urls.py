from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MlAlgorithmViewSet
from apps.endpoints.views import MlAlgorithmStatusViewSet
from apps.endpoints.views import MLRequestViewSet
from apps.endpoints.views import PredictView

'''
The urls visible at the ROOT API page 
'''
router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithm", MlAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MlAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")


urlpatterns = [
    url(r"", include(router.urls)),
    url(r"^api/v1", include(router.urls)),
    url(r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"),
]


