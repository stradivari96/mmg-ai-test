import pytest
from mmg_ai_test.averager import process_csv
from mmg_ai_test.constants import CSV_URL


def test_process_csv():
    res = process_csv(CSV_URL)
    assert res["lines"] == 10_906_858
    assert res["average"] == pytest.approx(1.750663)
