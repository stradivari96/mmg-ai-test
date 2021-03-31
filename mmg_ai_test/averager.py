from typing import TypedDict

import requests


class AveragerDict(TypedDict):
    lines: int
    average: float


def process_csv(url) -> AveragerDict:
    """
    Load the csv and calculate the number of lines and the average of the field 'tip_amount'
    """

    res = _request_stream(url)
    # TODO: Try other methods: boto3, dask, async approach?
    return res


def _request_stream(url: str):
    """"""
    lines, total = 0, 0
    with requests.get(url, stream=True) as r:
        iterator = r.iter_lines(decode_unicode=True)
        header = next(iterator)
        col = header.split(",").index("tip_amount")
        for line in iterator:
            if line:
                lines += 1
                total += float(line.split(",")[col])
    return {"lines": lines, "average": total / lines}
