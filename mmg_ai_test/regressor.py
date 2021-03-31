import joblib
import logging
import pandas as pd
from sklearn.linear_model import LinearRegression

from mmg_ai_test.constants import MODEL_FILE, FEATURES


class Model:
    """Wrapper for a machine learning model that predicts 'total_amount'."""

    def __init__(self):
        self._model = LinearRegression()

    def predict(self, x: dict) -> float:
        x = {f: x.get(f, 0) for f in FEATURES}
        df = pd.DataFrame(x, index=[0])
        return self._model.predict(df)[0]

    def train(self, df: pd.DataFrame):
        x = df[FEATURES]
        y = df["total_amount"]
        self._model.fit(x, y)

    def save(self, filename):
        joblib.dump(self, filename)

    @classmethod
    def load(cls, filename) -> "Model":
        try:
            model = joblib.load(filename)
        except FileNotFoundError:
            logging.warning("Model file not found, training a simple model")
            model = cls()
            df = pd.read_csv("./data/mmg_data_small.csv")
            model.train(df)
            model.save(MODEL_FILE)
        return model
