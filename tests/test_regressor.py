import pytest
import random
import pandas as pd
from mmg_ai_test.regressor import Model, features


def test_model_train_predict():
    m = Model()
    df = pd.DataFrame.from_dict(
        {f: [random.random() for _ in range(10)] for f in features}
    )
    df["total_amount"] = sum(df[f] for f in features)
    m.train(df)
    x = {f: random.random() for f in features}
    assert m.predict(x) == pytest.approx(sum(x.values()))
