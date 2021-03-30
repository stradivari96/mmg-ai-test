import requests
from typing import TypedDict

URI = "s3://mmg-hiring-tests/python/mmg_data.csv"
URL = "https://mmg-hiring-tests.s3-eu-west-1.amazonaws.com/python/mmg_data.csv"


class Result(TypedDict):
    lines: int
    average: float


def process_csv() -> Result:
    """
    Load the csv and calculate the number of lines and the average of the field 'tip_amount'
    """

    res = _process_stream(URL)
    # TODO: Try other methods
    # res = _process_dask(URI)
    return res


def _process_stream(url):
    col = None
    lines, total = 0, 0
    with requests.get(url, stream=True) as r:
        for line in r.iter_lines(decode_unicode=True):
            if col is None:
                col = line.split(",").index("tip_amount")
                continue
            if line:
                lines += 1
                total += float(line.split(",")[col])
    return {"lines": lines, "average": total / lines}
