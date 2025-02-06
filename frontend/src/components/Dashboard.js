// Dashboard.js

import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext';

const Dashboard = () => {
    const { user } = useContext(UserContext);

    return (
        <div>
            <h2>Welcome to Your Dashboard, {user.name}</h2>
            <div>
                <p><strong>Income:</strong> ${user.income}</p>
                <p><strong>Total Debt:</strong> ${user.total_debt}</p>
                <p><strong>Credit Score:</strong> {user.credit_score}</p>
                <p><strong>Number of Credit Cards:</strong> {user.num_credit_cards}</p>
            </div>
        </div>
    );
};

export default Dashboard;
