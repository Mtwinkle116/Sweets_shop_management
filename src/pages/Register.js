import { useState } from "react";
import { registerUser } from "../api/api";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const [form, setForm] = useState({
    username: "",
    password: "",
    first_name: "",
    last_name: "",
    email: "",
    is_admin: false,
  });

  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm({
      ...form,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await registerUser(form);
      setMessage("🎉 Registered Successfully! Redirecting to login...");
      setTimeout(() => navigate("/login"), 1500);
    } catch (err) {
      console.error("Registration Error:", err.response.data);
      setMessage("❌ Registration failed: " + JSON.stringify(err.response.data));
    }
  };

  return (
    <div className="form-container">
      <h2>Register</h2>
      {message && (
        <div style={{ textAlign: "center", color: "#6a1b9a", marginBottom: "1rem" }}>
          <strong>{message}</strong>
        </div>
      )}
      <form onSubmit={handleSubmit}>
        <input
          name="username"
          placeholder="Username"
          value={form.username}
          onChange={handleChange}
          required
        />
        <input
          name="password"
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          required
        />
        <input
          name="first_name"
          placeholder="First Name"
          value={form.first_name}
          onChange={handleChange}
        />
        <input
          name="last_name"
          placeholder="Last Name"
          value={form.last_name}
          onChange={handleChange}
        />
        <input
          name="email"
          type="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
        />
        <label>
          <input
            type="checkbox"
            name="is_admin"
            checked={form.is_admin}
            onChange={handleChange}
          />{" "}
          Is Admin?
        </label>
        <button type="submit">Register</button>
      </form>
    </div>
  );
}
