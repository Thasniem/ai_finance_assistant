// FinanceForm.js

import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

const FinanceForm = ({ onSubmit }) => {
    const [formData, setFormData] = useState({
        income: '',
        spending: '',
        credit_score: '',
        total_debt: ''
    });

    const history = useHistory();

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Send form data to the parent component for prediction
        onSubmit(formData);
        history.push("/prediction-result"); // Redirect to result page
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Income:</label>
                <input type="number" name="income" value={formData.income} onChange={handleChange} required />
            </div>
            <div>
                <label>Spending:</label>
                <input type="number" name="spending" value={formData.spending} onChange={handleChange} required />
            </div>
            <div>
                <label>Credit Score:</label>
                <input type="number" name="credit_score" value={formData.credit_score} onChange={handleChange} required />
            </div>
            <div>
                <label>Total Debt:</label>
                <input type="number" name="total_debt" value={formData.total_debt} onChange={handleChange} required />
            </div>
            <button type="submit">Submit</button>
        </form>
    );
};

export default FinanceForm;
