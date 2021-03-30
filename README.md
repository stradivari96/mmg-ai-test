# Python AI developers test

This is the MMG python tech test for new hirings.

## The Problem

We have a big csv to process located on this S3 bucket:

```
URL:
https://mmg-hiring-tests.s3-eu-west-1.amazonaws.com/python/mmg_data.csv
URI:
s3://mmg-hiring-tests/python/mmg_data.csv.
```

1. Our client wants an endpoint made in flask that will load the csv from this location and calculate the number of lines and the average of the field 'tip_amount'. The customer wants the most efficient solution possible.

2. Using this csv build a machine learning model that allows to make predictions about the total_amount field, and wrap it with an endpoint. The endpoint must receive the necessary values on which the model will work to make the prediction, must return this prediction and, in background, store it in a MongoDB.

   - Feel free to use a known pretrained model)
   - We dont matter the accuracy, is just to know that you are familiar with the technology)

3. Write a document explaining how you would solve the problem to someone with development skills in english

## Rules

- Make all the decisions you want.
- Share the solution as a link to a repo
- Ask anything you want to us, you have tech team emails
- The Document is one page doc limit

## License

[MIT](https://choosealicense.com/licenses/mit/)