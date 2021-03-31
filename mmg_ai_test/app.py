import json
from flask import Flask, request

from mmg_ai_test.averager import process_csv
from mmg_ai_test.regressor import Model
from mmg_ai_test.constants import CSV_URL

app = Flask(__name__)
model = Model.load("./data/model.joblib")


@app.route("/")
def average():
    r = process_csv(CSV_URL)
    return json.dumps(r)


@app.route("/predict")
def predict():
    pred = model.predict(request.args)
    return json.dumps({"prediction": pred})
