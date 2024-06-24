import joblib
import pandas as pd

class LinearRegression:
    def __init__(self):
        path_to_artifacts = "../../research/"
        #self.values_fill_missing =  joblib.load(path_to_artifacts + "train_mode.joblib")
        #self.encoders = joblib.load(path_to_artifacts + "encoders.joblib")
        self.model = joblib.load(path_to_artifacts + "linear_regression_D3.joblib")

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        input_data = pd.DataFrame(input_data, index=[0])

        return input_data
    
    def predict(self, input_data):
        return self.model.predict(input_data)
    
    def postprocessing(self, input_data):
        label = "normal"
        if input_data < 3.6:
            label = "low"
        if input_data > 20:
            label = "high"
        return {"1 Hour Later Chemical Oxygen": input_data, "status": label}
    
    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0].round(5)  # only one sample
            prediction = self.postprocessing(prediction)
        except Exception as e:
            #print(self.predict(input_data)[0].round(5))
            return {"status": "Error", "message": str(e)}

        return prediction
