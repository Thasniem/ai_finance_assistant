from flask import jsonify, request
from models.predictionModel import PredictionModel  # Corrected import
from services.mlService import predict_savings  # Corrected import

# Function to create and store a new prediction
def create_prediction(data):
    try:
        income = data.get("income")
        spending = data.get("spending")
        
        if income is None or spending is None:
            return {"error": "Income and spending are required"}, 400
        
        # Predict savings
        predicted_savings = predict_savings(income, spending)

        # Store prediction in the database
        new_prediction = PredictionModel(
            user_id=data.get("user_id"),
            income=income,
            spending=spending,
            predicted_savings=predicted_savings
        )
        new_prediction.save()

        return jsonify({"message": "Prediction created successfully", "predicted_savings": predicted_savings}), 201


    except Exception as e:
        return {"error": str(e)}, 500

# Function to get prediction by user ID
def get_prediction(user_id):
    try:
        prediction = PredictionModel.get_prediction_by_user(user_id)
        if prediction:
            return jsonify({"user_id": user_id, "predicted_savings": prediction}), 200
        else:
            return {"error": "No prediction found for this user"}, 404
    except Exception as e:
        return {"error": str(e)}, 500

# Route for making predictions based on user data
def make_prediction():
    try:
        data = request.get_json()
        return create_prediction(data)  # Reusing the create_prediction logic

    except Exception as e:
        return jsonify({"error": str(e)}), 500
