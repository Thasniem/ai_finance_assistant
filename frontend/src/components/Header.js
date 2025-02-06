// Header.js

import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
    return (
        <header>
            <h1>AI-Powered Personal Finance Assistant</h1>
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/dashboard">Dashboard</Link></li>
                    <li><Link to="/finance-form">Enter Finance Info</Link></li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
