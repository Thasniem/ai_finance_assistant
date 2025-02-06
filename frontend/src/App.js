// App.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './redux/store'; // Import the store

import Header from './components/Header';
import FinanceForm from './components/FinanceForm';
import PredictionResult from './components/PredictionResult';
import Dashboard from './components/Dashboard';

const App = () => {
    return (
        <Provider store={store}>
            <Router>
                <Header />
                <Switch>
                    <Route path="/" exact component={Dashboard} />
                    <Route path="/finance-form" component={FinanceForm} />
                    <Route path="/prediction-result" component={PredictionResult} />
                </Switch>
            </Router>
        </Provider>
    );
};

export default App;
