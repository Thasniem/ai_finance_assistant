#userRoutes
from flask import Blueprint
from controllers.userController import create_user, get_user, update_user

user_routes = Blueprint('user_routes', __name__)

# Route to create a new user
@user_routes.route('/user', methods=['POST'])
def add_user():
    return create_user()

# Route to get user information by ID
@user_routes.route('/user/<int:user_id>', methods=['GET'])  
def get_user_info(user_id):
    return get_user(user_id)

# Route to update user information
@user_routes.route('/user/<int:user_id>', methods=['PUT'])
def update_user_info(user_id):
    return update_user(user_id)
