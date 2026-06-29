import requests

print("===CRYPTO-PRICE-TRACKER===")

try:
    while True:
        coin = input("Enter cryptocurrency name (or 'exit' to quit): ").lower().strip()
        if coin == "exit":
            print("Task ended.")
            break
        
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        response = requests.get(url)
        
        if response.status_code == 200:
            params = {"crypto_id": coin, "currency": "usd"}

            response = requests.get(url, params=params)

            data = response.json()
            if coin in data:
                price = data[coin]["usd"]

                print("----- Result -----")
                print(f" Coin: {coin}\n Price: {price}")
                print("------------------")
            else:
                print("Coin not found. try\n dogecoin\n bitcoin\n ethereum")
        else:
            print("API request failed.")

    
except requests.exception.RequestException:
    print("Network error")