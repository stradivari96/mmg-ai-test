from typing import TypedDict

import requests


class AveragerDict(TypedDict):
    lines: int
    average: float


def process_csv(url, max_lines=None) -> AveragerDict:
    """Load the csv and return the number of lines and the average of the field 'tip_amount'."""

    res = _request_stream(url, max_lines)
    # TODO: Try other methods: boto3, dask, async approach?
    return res


def _request_stream(url: str, max_lines):
    """Request the csv via streaming and process it line by line."""
    lines, total = 0, 0
    with requests.get(url, stream=True) as r:
        iterator = r.iter_lines(decode_unicode=True)
        header = next(iterator)
        col = header.split(",").index("tip_amount")
        for line in iterator:
            if not line:
                continue
            lines += 1
            total += float(line.split(",")[col])
            if max_lines and lines >= max_lines:
                break
    return {"lines": lines, "average": total / lines}
