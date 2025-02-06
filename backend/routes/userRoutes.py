# userRoutes.py

from flask import Blueprint, request, jsonify
from controllers.userController import create_user, get_user, update_user

user_routes = Blueprint('user_routes', __name__)

# Route to create a new user
@user_routes.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    result = create_user(data)
    return jsonify(result), 201

# Route to get user information by ID
@user_routes.route('/user/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    result = get_user(user_id)
    return jsonify(result), 200

# Route to update user information
@user_routes.route('/user/<int:user_id>', methods=['PUT'])
def update_user_info(user_id):
    data = request.get_json()
    result = update_user(user_id, data)
    return jsonify(result), 200
