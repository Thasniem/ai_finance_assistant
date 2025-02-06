// PredictionResult.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const PredictionResult = () => {
    const [prediction, setPrediction] = useState(null);

    useEffect(() => {
        // Call backend API to get the prediction result
        axios.get('/api/predict')
            .then(response => {
                setPrediction(response.data.prediction);
            })
            .catch(error => {
                console.error("There was an error fetching the prediction!", error);
            });
    }, []);

    return (
        <div>
            <h2>Prediction Result</h2>
            {prediction ? (
                <div>
                    <p>Your predicted savings: ${prediction}</p>
                </div>
            ) : (
                <p>Loading prediction...</p>
            )}
        </div>
    );
};

export default PredictionResult;
