import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

features = [
    "fare_amount",
    "extra",
    "mta_tax",
    "tip_amount",
    "tolls_amount",
    "improvement_surcharge",
]


class Model:
    def __init__(self):
        self._model = LinearRegression()

    def predict(self, x):
        x = {f: x.get(f, 0) for f in features}
        df = pd.DataFrame(x, index=[0])
        return self._model.predict(df)[0]

    def train(self, df):
        x = df[features]
        y = df["total_amount"]
        self._model.fit(x, y)

    def save(self, filename):
        joblib.dump(self, filename)

    @classmethod
    def load(cls, filename):
        return joblib.load(filename)
