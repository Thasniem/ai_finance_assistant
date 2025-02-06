# predictionController.py

from flask import jsonify, request
from .models.predictionModel import PredictionModel  # Assuming you have a model to interact with ML
from .services.mlService import predict_savings  # Assuming you have a service function for prediction

# Route for making predictions based on user data
def make_prediction():
    try:
        data = request.get_json()
        income = data.get("income")
        spending = data.get("spending")
        
        if income is None or spending is None:
            return jsonify({"error": "Income and spending are required"}), 400
        
        # Using the service layer to make the prediction (adjust model as necessary)
        prediction = predict_savings(income, spending)
        
        return jsonify({"predicted_savings": prediction}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

