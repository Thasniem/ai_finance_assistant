from flask import Blueprint, request, jsonify
from controllers.transactionController import create_transaction, get_transactions, update_transaction

transaction_routes = Blueprint('transaction_routes', __name__)

# Route to create a new transaction
@transaction_routes.route('/transaction', methods=['POST'])
def add_transaction():
    data = request.get_json()
    result = create_transaction(data)
    return jsonify(result), 201

# Route to get all transactions for a user by user ID
@transaction_routes.route('/transactions/<int:user_id>', methods=['GET'])
def get_user_transactions(user_id):
    result = get_transactions(user_id)
    return jsonify(result), 200

# Route to update a transaction by ID
@transaction_routes.route('/transaction/<int:transaction_id>', methods=['PUT'])
def update_transaction_info(transaction_id):
    data = request.get_json()
    result = update_transaction(transaction_id, data)
    return jsonify(result), 200
