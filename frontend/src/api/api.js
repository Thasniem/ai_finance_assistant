import axios from 'axios';

// Set base URL from environment variables (Fallback: localhost)
const api = axios.create({
    baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000/api',
});

// Function to get the prediction result from the backend
export const getPrediction = async (formData) => {
    try {
        const response = await api.post('/predict', formData);
        return response.data;
    } catch (error) {
        console.error(" Error fetching prediction:", error.response?.data || error.message);
        return { error: "Failed to get prediction. Please try again." };
    }
};

// Fetch user details
export const getUserDetails = async (userId) => {
    try {
        const response = await api.get(`/users/${userId}`);
        return response.data;
    } catch (error) {
        console.error(" Error fetching user details:", error.response?.data || error.message);
        return { error: "Failed to fetch user details." };
    }
};

// Fetch user transactions
export const getTransactions = async (userId) => {
    try {
        const response = await api.get(`/transactions/${userId}`);
        return response.data;
    } catch (error) {
        console.error(" Error fetching transactions:", error.response?.data || error.message);
        return { error: "Failed to fetch transactions." };
    }
};

// Export API functions
export default {
    getPrediction,
    getUserDetails,
    getTransactions,
};
