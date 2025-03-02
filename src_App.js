import React, { useState, useEffect } from "react";
import axios from "axios";
import { Line } from "react-chartjs-2";

function App() {
  const [stockSymbol, setStockSymbol] = useState("AAPL");
  const [livePrice, setLivePrice] = useState(null);
  const [chartData, setChartData] = useState({ labels: [], datasets: [{ label: "Stock Price", data: [], borderColor: "blue", fill: false }] });

  useEffect(() => {
    const fetchLivePrice = async () => {
      const response = await axios.post("http://127.0.0.1:5000/live", { stock_symbol: stockSymbol });
      const price = response.data.live_price;

      setLivePrice(price);
      setChartData(prev => ({
        labels: [...prev.labels, new Date().toLocaleTimeString()],
        datasets: [{ ...prev.datasets[0], data: [...prev.datasets[0].data, price] }]
      }));
    };

    const interval = setInterval(fetchLivePrice, 10000);
    return () => clearInterval(interval);
  }, [stockSymbol]);

  return (
    <div className="container">
      <h2>📈 Live Stock Market Prediction</h2>
      <input type="text" placeholder="Enter Stock Symbol (e.g., AAPL)" value={stockSymbol} onChange={(e) => setStockSymbol(e.target.value.toUpperCase())} />
      <h3>Live Price: {livePrice ? `$${livePrice.toFixed(2)}` : "Loading..."}</h3>
      <Line data={chartData} />
    </div>
  );
}

export default App;
