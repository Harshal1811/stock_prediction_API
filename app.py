import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Get DATABASE_URL from Render environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

@app.route("/")
def home():
    return jsonify({"message": "Flask API is running successfully!"})

@app.route("/test-db")
def test_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        return jsonify({"message": "Database connected!", "timestamp": result[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
