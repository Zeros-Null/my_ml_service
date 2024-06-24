"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.linear_regression_3D import LinearRegression
from apps.ml.income_classifier.linear_regression import LinearRegression_NoDegree

try:
    registry = MLRegistry() # create ML registry
    # linear D=3
    rf = LinearRegression()
    # add to ML registry
    registry.add_algorithm(endpoint_name="Chemical Oxygen Prediction by 1 Hour Later",
                            algorithm_object=rf,
                            algorithm_name="linear regression",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Piotr",
                            algorithm_description="linear regression with Degree 3, Month 12",
                            algorithm_code=inspect.getsource(LinearRegression))
    
    # Linear 
    et = LinearRegression_NoDegree()
    # add to ML registry
    registry.add_algorithm(endpoint_name="Chemical Oxygen Prediction by 1 Hour Later",
                            algorithm_object=et,
                            algorithm_name="linear regression, no degree",
                            algorithm_status="testing",
                            algorithm_version="0.0.1",
                            owner="Piotr",
                            algorithm_description="Simple lienar regression, Month 12",
                            algorithm_code=inspect.getsource(LinearRegression_NoDegree))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
