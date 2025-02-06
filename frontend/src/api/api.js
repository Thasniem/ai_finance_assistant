// api.js

import axios from 'axios';

// Set base URL for the API
const api = axios.create({
    baseURL: 'http://localhost:5000/api', // Replace with your backend URL
});

// Function to get the prediction result from the backend
export const getPrediction = async (formData) => {
    try {
        const response = await api.post('/predict', formData);
        return response.data;
    } catch (error) {
        console.error("Error fetching prediction:", error);
        throw error;
    }
};

// You can add more API functions here if needed, such as user data, transactions, etc.
