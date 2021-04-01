# English Explanation

We need to create two endpoints in `Flask`:

- The first one has to fetch a remote csv and calculate the number of lines and the average `tip_amount`. To make it a bit more efficient we can process it line by line instead of downloading and loading the whole csv in memory. For this we can use the `requests` library and the `iter_lines` method.
- For the second enpoint we will first need to train a Machine Learning model (a simple Linear Regression from `sklearn` will do) and serialize it via `pickle`, `dill` or `joblib`. We can then load it at the start of the application so that the model is ready to make predictions. That prediction must also be stored in a `MongoDB` database, so we will also have to instantiate the client using `pymongo` to connect to it.
- As for type the endpoints, we can leave the first one as a `GET` request but the second one needs some inputs so we can either use query parameters or send them in the `body` of a `POST` request. The first option is simpler but it might be better the use a `POST` as storing the prediction makes it **not** `idempotent`.
- Some other things we might need to consider are related to the database, if we want both the app and the database in the same server we can dockerize the app and use `docker-compose` to link them together, another option might be to use some managed platforms such as `Mongodb Atlas`. All the secrets should be added to `.gitignore` and handled as environment variables instead.
- Last but not least, remember to handle the dependencies in an environment, create some tests, use a linter/autoformatter like `black` and follow the basic python conventions.
