import pytest
from mmg_ai_test.regressor import Model


def test_model():
    m = Model()
    assert m.predict({}) >= 0
