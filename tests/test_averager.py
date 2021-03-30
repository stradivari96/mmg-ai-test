import pytest
from mmg_ai_test.averager import process_csv


def test_process_csv():
    res = process_csv()
    assert res["lines"] == 10_906_858
    assert res["average"] == pytest.approx(1.750663)
