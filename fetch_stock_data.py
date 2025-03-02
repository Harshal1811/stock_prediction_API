import yfinance as yf
import psycopg2
from config import DATABASE_URL

# Connect to PostgreSQL
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

def fetch_and_store_stock(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")

    for index, row in data.iterrows():
        cur.execute(
            "INSERT INTO stock_data (symbol, date, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (symbol, index, row["Open"], row["High"], row["Low"], row["Close"], row["Volume"])
        )
    
    conn.commit()
    print(f"✅ Stock data for {symbol} stored successfully!")

if __name__ == "__main__":
    fetch_and_store_stock("AAPL")
