import yfinance as yf
import psycopg2

def fetch_and_store_stock_data(stock_symbol):
    # Connect to PostgreSQL
    conn = psycopg2.connect(database="stockdb", user="postgres", password="Harshal@1811", host="localhost", port="5432")
    cur = conn.cursor()

    # Fetch stock data (Last 1 day, 1-minute intervals)
    stock = yf.Ticker(stock_symbol)
    df = stock.history(period="1d", interval="1m")

    for index, row in df.iterrows():
        cur.execute("INSERT INTO stock_prices (stock_symbol, timestamp, close_price) VALUES (%s, %s, %s)",
                    (stock_symbol, index, row["Close"]))

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ {stock_symbol} Data Stored Successfully!")

# Example: Fetch Apple stock prices
fetch_and_store_stock_data("AAPL")
