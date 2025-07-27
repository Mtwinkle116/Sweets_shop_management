import { useEffect, useState } from "react";
import { getSweets, purchaseSweet } from "../api/api";
import SweetCard from "../components/SweetCard";

export default function Home() {
  const [sweets, setSweets] = useState([]);
  const [message, setMessage] = useState("");

  useEffect(() => {
    getSweets()
      .then((res) => setSweets(res.data))
      .catch((err) => {
        console.error(err);
        setMessage("Please login to view sweets.");
        setTimeout(() => (window.location.href = "/login"), 1500);
      });
  }, []);

  const handlePurchase = async (id, quantity) => {
    try {
      await purchaseSweet(id, quantity);
      setMessage("🎉 Purchase successful!");
      setTimeout(() => setMessage(""), 5000);
      const updated = await getSweets().then((res) => res.data);
      setSweets(updated);
    } catch (err) {
      console.error(err);
      setMessage("❌ Purchase failed. Try again!");
      setTimeout(() => setMessage(""), 5000);
    }
  };

  return (
  <>
    <div className="wave-background">
      <svg
        className="wave-svg"
        viewBox="0 0 1440 320"
        preserveAspectRatio="none"
      >
        <path
          fill="#bec3e7ff"
          d="M0,224L48,208C96,192,192,160,288,165.3C384,171,480,213,576,234.7C672,256,768,256,864,240C960,224,1056,192,1152,165.3C1248,139,1344,117,1392,106.7L1440,96L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"
        ></path>
      </svg>
    </div>
  
    {message && (
      <div
        style={{
          textAlign: "center",
          color: "#6a1b9a",
          marginTop: "1rem",
          position: "relative",
          zIndex: 20, // Ensures it stays on top of waves and cards
          backgroundColor: "#fefefe",
          padding: "0.75rem 1.5rem",
          borderRadius: "12px",
          width: "fit-content",
          marginLeft: "auto",
          marginRight: "auto",
          boxShadow: "0 4px 12px rgba(0, 0, 0, 0.1)",
          fontFamily: "'Poppins', sans-serif"
        }}
      >
        <strong>{message}</strong>
      </div>
    )}

  
    <div className="sweet-grid">
      {sweets.map((s) => (
        <SweetCard key={s.id} sweet={s} onPurchase={handlePurchase} />
      ))}
    </div>
  </>

  );
}
