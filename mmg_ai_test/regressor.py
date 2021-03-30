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
        ...

    def predict(self, x):
        return sum(x.get(f, 0) for f in features)
