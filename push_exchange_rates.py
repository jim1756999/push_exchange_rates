import requests
import json
import time

# fixer.io API key
API_ACCESS_KEY = "<PUT_YOUR_KEY_HERE>"

# Bark push key
PUSH_KEY = "<PUT_YOUR_KEY_HERE>"

# Get exchange rate from GBP to CNY from fixer.io API
def get_rates():
    url="http://data.fixer.io/api/latest?access_key=%s&symbols=CNY,GBP" %API_ACCESS_KEY
    r = requests.get(url)

    data = r.content

    data_dict = json.loads(data)
    rates_json = json.dumps(data_dict['rates'])
    rates_dict = json.loads(rates_json)

    rates = rates_dict['CNY'] / rates_dict['GBP']
    return rates

# Push to bark
def push(rates):
    push_url = "https://api.day.app/%s/GBP → CNY/%s" %(PUSH_KEY,rates)
    r = requests.get(push_url)
    print(r)

while True:
    rates = get_rates()
    push(rates)
    time.sleep(10000)
