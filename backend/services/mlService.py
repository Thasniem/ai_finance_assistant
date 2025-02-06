# mlService.py

import joblib
import os
from sklearn.preprocessing import StandardScaler

# Load the pre-trained model (adjust the path as necessary)
MODEL_PATH = os.path.join(os.getcwd(), 'model', 'finance_predictor.pkl')
model = joblib.load(MODEL_PATH)

# Load the scaler for feature scaling (if applicable)
scaler = joblib.load(os.path.join(os.getcwd(), 'model', 'scaler.pkl'))

# Function to preprocess the input data and make predictions
def predict_finance(data):
    try:
        # Assume data is a dictionary with necessary features for prediction
        features = [
            data['income'],
            data['spending'],
            data['credit_score'],
            data['total_debt']
            # Add more features as required by the model
        ]

        # Apply feature scaling if needed
        features_scaled = scaler.transform([features])

        # Get prediction from the model
        prediction = model.predict(features_scaled)
        
        # Return the prediction (for example, predicted savings)
        return {'prediction': prediction[0]}
    except Exception as e:
        return {'error': str(e)}

