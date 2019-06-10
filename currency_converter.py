import requests
import json


# Where USD is the base currency you want to use
url = 'https://api.exchangerate-api.com/v4/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

with open('currency.txt', 'w') as outfile:
    json.dump(data, outfile)
