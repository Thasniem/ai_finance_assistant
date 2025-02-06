# predictionRoutes.py

from flask import Blueprint, request, jsonify
from controllers.predictionController import create_prediction, get_prediction

prediction_routes = Blueprint('prediction_routes', __name__)

# Route to create a new prediction
@prediction_routes.route('/prediction', methods=['POST'])
def add_prediction():
    data = request.get_json()
    result = create_prediction(data)
    return jsonify(result), 201

# Route to get a prediction by user ID
@prediction_routes.route('/prediction/<int:user_id>', methods=['GET'])
def get_user_prediction(user_id):
    result = get_prediction(user_id)
    return jsonify(result), 200
