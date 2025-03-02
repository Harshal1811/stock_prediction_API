import pandas as pd
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

def train_model(stock_symbol):
    df = yf.Ticker(stock_symbol).history(period="5y")

    df["Date"] = df.index
    df["Day"] = df["Date"].dayofyear  # Convert date to numerical feature

    X = df[["Day"]]
    y = df["Close"]  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, f"{stock_symbol}_model.pkl")
    print(f"✅ {stock_symbol} Model Trained and Saved!")

# Train the model for Apple stock
train_model("AAPL")
