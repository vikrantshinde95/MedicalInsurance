from flask import Flask,render_template,jsonify,request
import config
from Project.utils import MedicalInsurance
import numpy as np

app = Flask(__name__)

@app.route("/")
def get_home():
    return render_template("index.html")

@app.route("/predict_charges",methods = ["POST","GET"])
def get_insurance():
    if request.method == "POST":
        data    = request.form 
        print("User input data is >>>>>>",data)
        age     = int(data["age"])
        Gender  = data["Gender"]
        bmi     =  eval(data["bmi"])
        children = int(data["children"])
        smoker = data["smoker"]
        region = data["region"]
        med_obj = MedicalInsurance(age,Gender,bmi,children,smoker,region)
        charges = med_obj.get_predicted_charges()
        return jsonify({"Result":f"Predicted Medical Insurance Price is {np.around(charges[0],2)}"})
    else:
        data    = request.form 
        print("User input data is >>>>>>",data)
        age     = int(data["age"])
        Gender  = data["Gender"]
        bmi     =  eval(data["bmi"])
        children = int(data["children"])
        print(">>>>>",data["smoker"])
        smoker = data["smoker"]
        region = data["region"]
        med_obj = MedicalInsurance(age,Gender,bmi,children,smoker,region)
        charges = med_obj.get_predicted_charges()
        return jsonify({"Result":f"Predicted Medical Insurance Price is {np.around(charges[0],2)}"})
    
    





if __name__ == "__main__":
    app.run()