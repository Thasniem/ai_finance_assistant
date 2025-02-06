// UserContext.js

import React, { createContext, useState } from 'react';

export const UserContext = createContext();

const UserProvider = ({ children }) => {
    const [user, setUser] = useState({
        name: 'John Doe',
        income: 50000,
        total_debt: 20000,
        credit_score: 700,
        num_credit_cards: 3
    });

    return (
        <UserContext.Provider value={{ user, setUser }}>
            {children}
        </UserContext.Provider>
    );
};

export default UserProvider;
