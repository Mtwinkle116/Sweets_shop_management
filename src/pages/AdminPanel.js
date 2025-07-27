import { useEffect, useState } from "react";
import { createSweet, updateSweet, deleteSweet } from "../api/api";
import axios from "axios";

export default function AdminPanel() {
  const [form, setForm] = useState({ name: "", category: "", price: "", quantity: "" });
  const [isAdmin, setIsAdmin] = useState(null);
  const [message, setMessage] = useState("");

  const token = localStorage.getItem("token");

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/auth/me/", {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((res) => {
        if (res.data.is_admin) setIsAdmin(true);
        else setIsAdmin(false);
      })
      .catch(() => setIsAdmin(false));
  }, []);

  const showMessage = (msg) => {
    setMessage(msg);
    setTimeout(() => setMessage(""), 5000);
  };

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleCreate = () => {
    createSweet(form).then(() => showMessage("🎂 Sweet Created Successfully!"));
  };

  const handleUpdate = () => {
    const { id, ...rest } = form;
    const filteredData = Object.fromEntries(Object.entries(rest).filter(([_, value]) => value !== ""));
    if (!id) return showMessage("⚠️ ID is required for update");
    updateSweet(id, filteredData).then(() => showMessage("✅ Sweet Updated"));
  };

  const handleDelete = () => {
    deleteSweet(form.id).then(() => showMessage("🗑️ Sweet Deleted"));
  };

  if (isAdmin === null) return <p>Checking permissions...</p>;
  if (!isAdmin) return <p>You are not an admin.</p>;

  return (
    <div className="form-container">
      <h2>Admin Panel</h2>
      {message && (
        <div style={{ textAlign: "center", color: "#6a1b9a", marginBottom: "1rem" }}>
          <strong>{message}</strong>
        </div>
      )}
      <input name="id" placeholder="ID (for update/delete)" onChange={handleChange} />
      <input name="name" placeholder="Sweet Name" onChange={handleChange} />
      <input name="category" placeholder="Category" onChange={handleChange} />
      <input name="price" placeholder="Price" onChange={handleChange} />
      <input name="quantity" placeholder="Quantity" onChange={handleChange} />
      <div className="button-group">
        <button onClick={handleCreate}>Create</button>
        <button onClick={handleUpdate}>Update</button>
        <button onClick={handleDelete}>Delete</button>
      </div>
    </div>
  );
}
