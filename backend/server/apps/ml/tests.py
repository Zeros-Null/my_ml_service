# add at the beginning of the file:
import inspect
from apps.ml.registry import MLRegistry


from django.test import TestCase

from apps.ml.income_classifier.linear_regression_3D import LinearRegression
from apps.ml.income_classifier.linear_regression import LinearRegression_NoDegree

class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            "Hour": 3,
            "[水]-溶解氧 (mg/L)": 7.5
        }
        my_alg = LinearRegression()
        response = my_alg.compute_prediction(input_data)
        self.assertTrue('normal', response['status'])
        self.assertEqual(7.51339, response['1 Hour Later Chemical Oxygen'])
        print(response)

 #add below method to MLTests class:
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "Chemical Oxygen Prediction by 1 Hour Later"
        algorithm_object = LinearRegression()
        algorithm_name = "linear regression"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Piotr"
        algorithm_description = "Linear Regression with Degree 3, Month 12"
        algorithm_code = inspect.getsource(LinearRegression)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)

    

