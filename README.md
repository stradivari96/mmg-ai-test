# Python AI developers test
[![codecov](https://codecov.io/gh/stradivari96/mmg-ai-test/branch/main/graph/badge.svg?token=NKCRH5K75Y)](https://codecov.io/gh/stradivari96/mmg-ai-test)

## Installation
This project uses [poetry](https://python-poetry.org/) for dependency management.
```
poetry install
```
You can also install the requirements directly:
```
pip install -r requirements.txt
```

## Running
To run the endpoint locally:
```
python scripts/run.py
```
You should be able to test it using curl:
```
curl "localhost:5000/"
curl "localhost:5000/predict?tip_amount=5&extra=3"
```
