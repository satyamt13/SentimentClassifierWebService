"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

import inspect
from apps.ml.sentimentClassifier.CLSTM import CLSTM
from apps.ml.registry import MlRegistry

try:
    registry = MlRegistry()
    clstm = CLSTM()
    registry.add_algorithm(
        endpoint_name="sentiment_classifier",
        algorithm_object=clstm,
        algorithm_name = "CLSTM",
        algorithm_status="production",
        algorithm_version="0.0.1",
        owner="Luci4",
        algorithm_description="""C-LSTM(Zhou Et al. 2015) sentiment classifier with Phrases2Vec embedding layer
         trained on over 1 million Amazon movies & T.V. reviews""",
        algorithm_code=inspect.getsource(CLSTM)
    )
except Exception as e:
    print("Error while loading the algorithms to the registry", str(e))



