import { useContext, useState } from "react";
import { loginUser } from "../api/api";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

export default function Login() {
  const [form, setForm] = useState({ username: "", password: "" });
  const [message, setMessage] = useState("");
  const navigate = useNavigate();
  const { login } = useContext(AuthContext);

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const { data } = await loginUser(form);
      login(data.access);
      localStorage.setItem("refresh", data.refresh);
      setMessage("✅ Logged in successfully! Redirecting...");
      setTimeout(() => navigate("/"), 1500);
    } catch (err) {
      console.error("Login Error:", err.response?.data);
      setMessage("❌ Login failed. Please check your credentials.");
    }
  };

  return (
    <div className="form-container">
      <h2>Login</h2>
      {message && (
        <div style={{ textAlign: "center", color: "#6a1b9a", marginBottom: "1rem" }}>
          <strong>{message}</strong>
        </div>
      )}
      <form onSubmit={handleSubmit}>
        <input name="username" placeholder="Username" onChange={handleChange} />
        <input
          name="password"
          type="password"
          placeholder="Password"
          onChange={handleChange}
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}
