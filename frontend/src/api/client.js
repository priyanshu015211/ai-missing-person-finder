import axios from "axios";

const apiClient = axios.create({
  baseURL:
    import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api/v1",
  timeout: 5000,
  headers: {
    Accept: "application/json",
  },
});

export function getApiHealth() {
  return apiClient.get("/health");
}

export default apiClient;
