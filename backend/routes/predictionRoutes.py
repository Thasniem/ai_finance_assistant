from flask import Blueprint, request, jsonify
from backend.controllers.predictionController import create_prediction, get_prediction, make_prediction

prediction_routes = Blueprint('prediction_routes', __name__)

# Route to create a new prediction
@prediction_routes.route('/prediction', methods=['POST'])
def add_prediction():
    data = request.get_json()
    result, status = create_prediction(data)
    return jsonify(result), status

# Route to get a prediction by user ID
@prediction_routes.route('/prediction/<int:user_id>', methods=['GET'])
def get_user_prediction(user_id):
    result, status = get_prediction(user_id)
    return jsonify(result), status
