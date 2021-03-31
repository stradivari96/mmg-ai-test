import pytest
import random
import pandas as pd
from mmg_ai_test.regressor import Model
from mmg_ai_test.constants import FEATURES


def test_model_train_predict():
    m = Model()
    df = pd.DataFrame.from_dict(
        {f: [random.random() for _ in range(10)] for f in FEATURES}
    )
    df["total_amount"] = sum(df[f] for f in FEATURES)
    m.train(df)
    x = {f: random.random() for f in FEATURES}
    assert m.predict(x) == pytest.approx(sum(x.values()))
