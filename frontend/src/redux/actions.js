// actions.js

// Define action types
export const SET_USER_DATA = 'SET_USER_DATA';

// Action to set user data in the Redux store
export const setUserData = (userData) => {
    return {
        type: SET_USER_DATA,
        payload: userData
    };
};

// Action for prediction results
export const SET_PREDICTION_RESULT = 'SET_PREDICTION_RESULT';

// Action to set prediction result
export const setPredictionResult = (prediction) => {
    return {
        type: SET_PREDICTION_RESULT,
        payload: prediction
    };
};
