import React, { useState } from "react";

const StockForm = ({ fetchStock }) => {
  const [symbol, setSymbol] = useState("");

  return (
    <div>
      <input
        type="text"
        value={symbol}
        onChange={(e) => setSymbol(e.target.value)}
        placeholder="Enter Stock Symbol"
      />
      <button onClick={() => fetchStock(symbol)}>Fetch Stock</button>
    </div>
  );
};

export default StockForm;
