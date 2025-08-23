import requests

BASE_URL = "http://127.0.0.1:8000/data"

# New row data (keys must match your CSV columns exactly)
new_row = {
    "Date ": "22-Aug-2025",
    "series ": "EQ",
    "OPEN ": "1,420.00",
    "HIGH ": "1,423.40",
    "LOW ": "1,407.90",
    "PREV. CLOSE ": "1,424.80",
    "ltp ": "1,409.90",
    "close ": "1,409.20",
    "vwap ": "1,414.00",
    "52W H ": "3,079.45",
    "52W L ": "1,114.85",
    "VOLUME ": "58,18,868",
    "VALUE ": "8,22,78,76,997.30",
    "No of trades ": "1,37,165"
}

# Insert row into API (which also updates CSV)
response = requests.delete(f"{BASE_URL}/0")

print("\n--- Insert Row Response ---")
print(response.json())
