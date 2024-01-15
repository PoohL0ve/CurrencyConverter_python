import requests
import json 

# Endpoit URL for the currency
endpoint = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"

# data of the reource
data = requests.get(endpoint)
results = json.loads(data.text)

print(results)