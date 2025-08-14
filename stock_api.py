import requests
import json

def fetch_data(url):
    try:
        response = requests.get(url=url)
        data = response.json()
        if data["success"] and "data" in data:
            page_data = data["data"]
            #print("page_data:", page_data)
            stock_data = page_data.get("data", [])
            for stock in stock_data:
                stock_names = stock.get("Name")
                stock_symbols = stock.get("Symbol")
                stock_marketcap = stock.get("MarketCap")
                print(f"Stock Names: {stock_names}, \nSymbols: {stock_symbols}, \nMarket Cap: {stock_marketcap}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        
if __name__=="__main__":
    url = "https://api.freeapi.app/api/v1/public/stocks"  # Replace with the actual API URL
    result = fetch_data(url)
    if result:
        print(result)
    else:
        print("No data found or an error occurred.")