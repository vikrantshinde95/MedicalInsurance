import pickle
import json
import config
import numpy as np

class MedicalInsurance():
    def __init__(self,age,Gender,bmi,children,smoker,region):
        self.age = age
        self.Gender = Gender
        self.bmi = bmi
        self.children = children
        self.smoker = smoker.lower()
        self.region = "region_" + region.lower()
    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as file:
            self.model = pickle.load(file)

        with open(config.JSON_FILE_PATH,"r") as file:
            self.json_data = json.load(file)
    def get_predicted_charges(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data["columns"])) # 8
        test_array[0] = self.age
        test_array[1] = self.json_data["Gender"][self.Gender]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data["smoker"][self.smoker]
        region_index = self.json_data["columns"].index(self.region)
        test_array[region_index] = 1
        predict_charges = self.model.predict([test_array])
        return predict_charges

