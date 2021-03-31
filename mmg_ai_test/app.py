import json
import logging

from flask import Flask, request
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from mmg_ai_test.averager import process_csv
from mmg_ai_test.regressor import Model
from mmg_ai_test.constants import CSV_URL, MODEL_FILE

app = Flask(__name__)
model = Model.load(MODEL_FILE)

# TODO: use env variables
client = MongoClient(
    "mongodb", username="root", password="rootpassword", serverSelectionTimeoutMS=5000
)
db = client.database
collection = db.predictions

try:
    client.admin.command("ismaster")
    logging.warning("Connected to MongoDB")
except ConnectionFailure:
    collection = None
    logging.warning("Can't connect to MongoDB")


@app.route("/")
def average():
    r = process_csv(CSV_URL)
    return json.dumps(r)


@app.route("/predict")
def predict():
    pred = model.predict(request.args)
    d = {"prediction": pred}
    if collection:
        collection.insert_one(d)
        d.pop("_id")
    return json.dumps(d)
