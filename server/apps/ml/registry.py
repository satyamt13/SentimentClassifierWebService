from apps.endpoints.models import Endpoint
from apps.endpoints.models import MlAlgorithm
from apps.endpoints.models import MlAlgorithmStatus

class MlRegistry:
    def __init__(self):
        self.endpoints = {}

    def add_algorithm(self, endpoint_name, algorithm_object, algorithm_name,
                      algorithm_status, algorithm_version, owner,
                      algorithm_description, algorithm_code):
        endpoint, _ = Endpoint.objects.get_or_create(name=endpoint_name, owner=owner)
        databse_object, algorithm_created = MlAlgorithm.objects.get_or_create(
            name=algorithm_name,
            description=algorithm_description,
            code=algorithm_code,
            version=algorithm_version,
            owner=owner,
            parentEndpoint=endpoint
        )
        if algorithm_created:
            status = MlAlgorithmStatus(
                status=algorithm_status,
                createdBy=owner,
                parentAlgorithm=databse_object,
                active=True
            )
            status.save()
        self.endpoints[databse_object.id] = algorithm_object
