import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))
columns_name = pickle.load(open("columns_name.pkl", "rb"))
car_list = pd.read_csv('car_list.csv')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods = ["POST","GET"])
def predict():
    model_name = request.form['Model']
    mileage = request.form['Mileage']
    year = request.form['Year']
    manufacturer = car_list.set_index('model')['manufacturer'][model_name].mode()[0]
    fuel =  car_list.set_index('model')['fuel'][model_name].mode()[0]
    cylinders = car_list.set_index('model')['cylinders'][model_name].mode()[0]
    transmission = car_list.set_index('model')['transmission'][model_name].mode()[0]
    type = car_list.set_index('model')['type'][model_name].mode()[0]
    drive =car_list.set_index('model')['drive'][model_name].mode()[0]
    
    arr = [[model_name, manufacturer, year, mileage, fuel, cylinders, transmission, type, drive]]
    newdata = pd.DataFrame(arr, columns=columns_name)

    scaled = encoder.fit_transform(newdata)
    prediction = model.predict(scaled)
    show_pre = int(np.expm1(prediction))
    return render_template("predict.html", data=show_pre) #그래프로 보이게 수정


if __name__ == "__main__":
    app.run(debug=True)