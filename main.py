import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
response = requests.get(url)

coin = input("Enter cryptocurrency name: ").lower().strip()
params = {"crypto_id": coin, "currency": "usd"}

response = requests.get(url, params=params)

data = response.json()
price = data[coin]["usd"]

print("----- Result -----")
print(f" Coin: {coin}\n Price: {price}")
print("------------------")