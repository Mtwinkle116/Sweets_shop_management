import { useState } from "react";
import "./../styles/main.css";

export default function SweetCard({ sweet, onPurchase }) {
  const [qty, setQty] = useState(1);

  return (
    <div className="sweet-card">
      <h3>{sweet.name}</h3>
      <p>₹{sweet.price}</p>
      <p>{sweet.category}</p>
      <p>Stock: {sweet.quantity}</p>

      <input
        className="qty-input"
        type="number"
        min="1"
        max={sweet.quantity}
        value={qty}
        onChange={(e) => setQty(Number(e.target.value))}
      />


      <button
        onClick={() => onPurchase(sweet.id, qty)}
        disabled={sweet.quantity === 0 || qty < 1}
      >
        {sweet.quantity > 0 ? "Buy Now" : "Out of Stock"}
      </button>
    </div>
  );
}
