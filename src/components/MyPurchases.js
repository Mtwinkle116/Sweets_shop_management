import { useEffect, useState } from "react";
import axios from "axios";

export default function MyPurchases() {
  const [purchases, setPurchases] = useState([]);
  const token = localStorage.getItem("token");

  useEffect(() => {
    axios.get("http://localhost:8000/api/user/purchases/", {
      headers: { Authorization: `Bearer ${token}` },
    }).then((res) => setPurchases(res.data));
  }, []);

  return (
    <div className="form-container">
      <h2>My Purchases</h2>
      {purchases.length === 0 ? (
        <p>No purchases yet.</p>
      ) : (
        purchases.map((item, index) => (
          <div key={index}>
            <p><strong>{item.sweet.name}</strong> - Quantity: {item.quantity}</p>
          </div>
        ))
      )}
    </div>
  );
}
