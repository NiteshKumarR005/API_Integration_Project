import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
response = requests.get(url)

coin = "bitcoin"
params = {"hello": coin, "currency": "usd"}

response = requests.get(url, params=params)

data = response.json()
print(data)