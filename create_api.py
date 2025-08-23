from fastapi import FastAPI, HTTPException
import pandas as pd
import os

app = FastAPI()

CSV_FILE = "Quote-Equity-RELIANCE-EQ-23-08-2024-to-23-08-2025.csv"

# Load CSV (or create empty DataFrame if not exists)
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
else:
    df = pd.DataFrame()

def save_csv():
    df.to_csv(CSV_FILE, index=False)

@app.get("/")
def home():
    return {"message": "CSV API with CRUD is running!"}

# ---------------- READ ----------------
@app.get("/data")
def get_data():
    return df.to_dict(orient="records")

@app.get("/data/{row_id}")
def get_row(row_id: int):
    if row_id >= len(df) or row_id < 0:
        raise HTTPException(status_code=404, detail="Row not found")
    return df.iloc[row_id].to_dict()

# ---------------- CREATE ----------------
@app.post("/data")
def create_row(row: dict):
    global df
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    save_csv()
    return {"message": "Row added successfully", "data": row}

# ---------------- UPDATE ----------------
@app.put("/data/{row_id}")
def update_row(row_id: int, row: dict):
    global df
    if row_id >= len(df) or row_id < 0:
        raise HTTPException(status_code=404, detail="Row not found")
    for key, value in row.items():
        if key in df.columns:
            df.at[row_id, key] = value
    save_csv()
    return {"message": "Row updated successfully", "data": df.iloc[row_id].to_dict()}

# ---------------- DELETE ----------------
@app.delete("/data/{row_id}")
def delete_row(row_id: int):
    global df
    if row_id >= len(df) or row_id < 0:
        raise HTTPException(status_code=404, detail="Row not found")
    deleted = df.iloc[row_id].to_dict()
    df = df.drop(row_id).reset_index(drop=True)
    save_csv()
    return {"message": "Row deleted successfully", "deleted": deleted}
