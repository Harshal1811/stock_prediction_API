import React, { useState } from "react";
import axios from "axios";
import StockForm from "./components/StockForm";
import StockData from "./components/StockData";

function App() {
  const [data, setData] = useState(null);

  const fetchStock = async (symbol) => {
    const response = await axios.get(`https://your-api.onrender.com/fetch-stock/${symbol}`);
    setData(response.data);
  };

  return (
    <div>
      <h1>Stock Market Tracker</h1>
      <StockForm fetchStock={fetchStock} />
      {data && <StockData data={data} />}
    </div>
  );
}

export default App;
