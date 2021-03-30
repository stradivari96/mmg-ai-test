import json
from flask import Flask

from mmg_ai_test.averager import process_csv
from mmg_ai_test.models import Model

app = Flask(__name__)
model = Model()


@app.route("/")
def average():
    r = process_csv()
    return json.dumps(r)


@app.route("/predict", methods=["POST"])
def predict():
    r = model.predict()
    return json.dumps(r)


if __name__ == "__main__":
    app.run()
