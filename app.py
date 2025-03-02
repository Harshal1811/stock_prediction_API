from flask import Flask, request, jsonify
import joblib
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# PostgreSQL Connection
conn = psycopg2.connect(database="stockDB", user="postgres", password="your_password", host="localhost", port="5432")
cur = conn.cursor()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    stock_symbol = data["stock_symbol"]

    model = joblib.load(f"{stock_symbol}_model.pkl")
    prediction = model.predict([[365]])  # Predict 1 year ahead

    return jsonify({"stock_symbol": stock_symbol, "predicted_price": prediction[0]})

@app.route("/live", methods=["POST"])
def live_stock():
    data = request.get_json()
    stock_symbol = data["stock_symbol"]

    cur.execute("SELECT close_price FROM stock_prices WHERE stock_symbol = %s ORDER BY timestamp DESC LIMIT 1", (stock_symbol,))
    live_price = cur.fetchone()[0]

    return jsonify({"stock_symbol": stock_symbol, "live_price": live_price})

if __name__ == "__main__":
    app.run(debug=True)
