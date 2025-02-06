// store.js

import { createStore, combineReducers } from 'redux';
import { userReducer, predictionReducer } from './reducers';

// Combine reducers (you can add more reducers if needed)
const rootReducer = combineReducers({
    user: userReducer,
    prediction: predictionReducer
});

// Create Redux store
const store = createStore(
    rootReducer,
    // Uncomment the line below if you're using Redux DevTools in your browser
    // window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

export default store;
