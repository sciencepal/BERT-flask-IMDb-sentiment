# BERT-flask-IMDb-sentiment

## What this project does

This project trains the BERT-base-uncased transformer model from huggingface library on the 50,000 IMDb movie reviews dataset and uses Flask to expose an API for sentiment analysis of any statement / movie review.

## How to set it up

1. Run train.py file - training runs for 10 epochs and generates model.bin file (preferably on a GPU)
2. Run app.py to expose the endpoint
3. Visit the endpoint and give your sentence to the API to get sentiment

### This code is copied and slightly modified from Abhihek Thakur's BERT sentiment analysis
