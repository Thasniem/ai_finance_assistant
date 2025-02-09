import joblib
import os
import numpy as np
from datetime import datetime
from sklearn.preprocessing import StandardScaler

# Define paths for model and scaler
MODEL_DIR = os.path.join(os.getcwd(), 'model')
MODEL_PATH = os.path.join(MODEL_DIR, 'finance_predictor.pkl')
SCALER_PATH = os.path.join(MODEL_DIR, 'scaler.pkl')

# Load the model and scaler
try:
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        raise FileNotFoundError("Model or scaler file is missing. Ensure they are placed in the 'model' directory.")

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

except Exception as e:
    raise RuntimeError(f"Error loading model or scaler: {str(e)}")

def clean_numeric(value):
    """Converts string values (with '$' or commas) into float."""
    try:
        return float(value.replace("$", "").replace(",", ""))
    except ValueError:
        return None

def preprocess_transaction(transaction):
    """
    Prepares transaction data for prediction.
    
    :param transaction: Dictionary containing transaction details.
    :return: Processed feature array or error message.
    """
    try:
        required_fields = ['amount', 'mcc', 'use_chip']
        missing_fields = [field for field in required_fields if field not in transaction]

        if missing_fields:
            return {'error': f"Missing required transaction fields: {', '.join(missing_fields)}"}

        amount = clean_numeric(transaction.get('amount', '0'))
        mcc = int(transaction.get('mcc', 0))
        use_chip = 1 if transaction.get('use_chip', '').lower() == "chip transaction" else 0

        return [amount, mcc, use_chip]

    except Exception as e:
        return {'error': f"Transaction preprocessing error: {str(e)}"}

def preprocess_user(user):
    """
    Prepares user financial data for prediction.
    
    :param user: Dictionary containing user details.
    :return: Processed feature array or error message.
    """
    try:
        required_fields = ['income', 'spending', 'credit_score', 'total_debt']
        missing_fields = [field for field in required_fields if field not in user]

        if missing_fields:
            return {'error': f"Missing required user fields: {', '.join(missing_fields)}"}

        income = clean_numeric(user.get('income', '0'))
        spending = clean_numeric(user.get('spending', '0'))
        credit_score = int(user.get('credit_score', 0))
        total_debt = clean_numeric(user.get('total_debt', '0'))

        return [income, spending, credit_score, total_debt]

    except Exception as e:
        return {'error': f"User preprocessing error: {str(e)}"}

def predict_finance(user_data, transaction_data):
    """
    Predicts financial trends based on user and transaction data.

    :param user_data: Dictionary with user financial details.
    :param transaction_data: Dictionary with transaction details.
    :return: Dictionary containing the prediction or error message.
    """
    try:
        # Preprocess user and transaction data
        user_features = preprocess_user(user_data)
        transaction_features = preprocess_transaction(transaction_data)

        # Check if any preprocessing step returned an error
        if isinstance(user_features, dict) and 'error' in user_features:
            return user_features
        if isinstance(transaction_features, dict) and 'error' in transaction_features:
            return transaction_features

        # Combine user and transaction features
        features = np.array(user_features + transaction_features).reshape(1, -1)

        # Apply feature scaling
        features_scaled = scaler.transform(features)

        # Get prediction
        prediction = model.predict(features_scaled)[0]

        return {'prediction': float(prediction)}

    except Exception as e:
        return {'error': str(e)}
