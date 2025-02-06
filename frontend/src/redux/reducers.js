// reducers.js

import { SET_USER_DATA, SET_PREDICTION_RESULT } from './actions';

// Initial state for the Redux store
const initialState = {
    user: {},
    prediction: null
};

// User reducer to handle user data
export const userReducer = (state = initialState.user, action) => {
    switch (action.type) {
        case SET_USER_DATA:
            return action.payload;
        default:
            return state;
    }
};

// Prediction reducer to handle prediction results
export const predictionReducer = (state = initialState.prediction, action) => {
    switch (action.type) {
        case SET_PREDICTION_RESULT:
            return action.payload;
        default:
            return state;
    }
};
