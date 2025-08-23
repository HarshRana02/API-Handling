# 📈 Stock API

A simple Python project that fetches stock market data, provides a FastAPI-powered CSV API, and allows global hosting with **ngrok**.

---

## 🚀 Features

- Fetches stock market data from a public API
- Provides a **FastAPI**-based CSV API for CRUD operations
- Parses JSON responses for stock info (name, symbol, market cap)
- Expose your local API to the internet using **ngrok**
- Easy to extend and integrate

---

## 🧰 Requirements

- Python 3.x
- Internet connection
- `requests`, `fastapi`, `uvicorn`, `pandas`
- `ngrok` (for global hosting)

---

## 📦 Get Start

### 1. Clone the Repository
<pre>
git clone https://github.com/HarshRana02/API-Handling.git
cd API-Handling
</pre>

### 2. Install Dependencies
<pre>
pip install -r requirements.txt
</pre>

### 3. Setup ngrok
<pre>
Visit https://ngrok.com/
Download .zip file in project folder and extract it. 
Add .exe in Environmental Variable: PATH

Create an account in ngrok.
Copy your Auth Token from dashboard.
ngrok config add-authtoken <YOUR_TOKEN> 

In your project folder, start your API: python -m uvicorn main:app --host 0.0.0.0 --port 8000

Start ngrok Tunnel: ngrok http 8000

Visit: https://abcd-1234.ngrok-free.app/data
</pre>