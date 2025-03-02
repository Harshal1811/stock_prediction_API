CREATE TABLE stock_data (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    date TIMESTAMP,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume INT
);
