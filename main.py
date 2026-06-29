import requests

try:
    

    while True:
        coin = input("Enter cryptocurrency name (or 'exit' to quit): ").lower().strip()
        if coin == "exit":
            print("Task ended.")
            break
        
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        response = requests.get(url)
        
        params = {"crypto_id": coin, "currency": "usd"}

        response = requests.get(url, params=params)

        data = response.json()
        if coin in data:
            price = data[coin]["usd"]

            print("----- Result -----")
            print(f" Coin: {coin}\n Price: {price}")
            print("------------------")
        else:
            print("Coin not found.")
    
except requests.exception.RequestException:
    print("Network error")