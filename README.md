# Python AI developers test
![test](https://github.com/stradivari96/mmg-ai-test/actions/workflows/test.yml/badge.svg)
[![codecov](https://codecov.io/gh/stradivari96/mmg-ai-test/branch/main/graph/badge.svg?token=NKCRH5K75Y)](https://codecov.io/gh/stradivari96/mmg-ai-test)

## Running
To run the endpoint locally use `docker-compose`:
```
docker-compose up -d
```
If you don't have docker, you can do:
```
# Note: won't insert into MongoDB
FLASK_APP=mmg_ai_test/app.py flask run
```
You should be able to test it using curl:
```
curl "localhost:5000/"
curl "localhost:5000/predict?tip_amount=5&extra=3"
```

## Development
This project uses [poetry](https://python-poetry.org/) for dependency management.
```
poetry install
```
You can also install the requirements directly:
```
pip install -r requirements.txt
```
