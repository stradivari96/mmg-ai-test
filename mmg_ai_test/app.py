import json
from flask import Flask, request

from mmg_ai_test.averager import process_csv
from mmg_ai_test.regressor import Model

app = Flask(__name__)
model = Model.load("./data/model.joblib")

URL = "https://mmg-hiring-tests.s3-eu-west-1.amazonaws.com/python/mmg_data.csv"


@app.route("/")
def average():
    r = process_csv(URL)
    return json.dumps(r)


@app.route("/predict")
def predict():
    pred = model.predict(request.args)
    return json.dumps({"prediction": pred})
