import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// ✅ Automatically attach token from localStorage if available
API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const registerUser = (data) => API.post('/auth/register/', data);
export const loginUser = (data) => API.post('/auth/login/', data);

// ✅ Sweets
export const getSweets = () => API.get('/sweets/');
export const createSweet = (data) => API.post('/sweets/', data);
export const updateSweet = (id, data) => API.put(`/sweets/${id}/`, data);
export const deleteSweet = (id) => API.delete(`/sweets/${id}/delete/`);
export const searchSweets = (query) => API.get(`/sweets/search/?query=${query}`);
export const purchaseSweet = (id, quantity) =>
  API.post(`/sweets/${id}/purchase/`, { quantity });
