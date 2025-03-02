import os
import psycopg2
from flask import Flask, jsonify
from config import DATABASE_URL
from fetch_stock_data import fetch_and_store_stock

app = Flask(__name__)

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    print("✅ Connected to the database successfully!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")

@app.route("/")
def home():
    return jsonify({"message": "Flask API is running successfully!"})

@app.route("/fetch-stock/<symbol>")
def fetch_stock(symbol):
    fetch_and_store_stock(symbol)
    return jsonify({"message": f"Stock data for {symbol} stored successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
