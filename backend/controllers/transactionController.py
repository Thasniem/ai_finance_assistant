# transactionController.py

from flask import jsonify, request
from .models.transactionModel import TransactionModel  # Assuming a transaction model for MongoDB

# Route for creating a new transaction
def create_transaction():
    try:
        data = request.get_json()
        
        client_id = data.get("client_id")
        card_id = data.get("card_id")
        amount = data.get("amount")
        
        if client_id is None or card_id is None or amount is None:
            return jsonify({"error": "Client ID, Card ID, and Amount are required"}), 400
        
        # Create the transaction object
        transaction = TransactionModel(
            client_id=client_id,
            card_id=card_id,
            amount=amount,
            date=data.get("date"),
            merchant_id=data.get("merchant_id"),
            merchant_city=data.get("merchant_city"),
            merchant_state=data.get("merchant_state"),
            zip_code=data.get("zip"),
            mcc=data.get("mcc"),
            errors=data.get("errors")
        )
        
        # Save to database
        transaction.save()
        
        return jsonify({
            "message": "Transaction created successfully",
            "transaction": {
                "transaction_id": transaction.id,
                "amount": transaction.amount,
                "date": transaction.date
            }
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route for getting transactions for a specific user
def get_user_transactions(user_id):
    try:
        transactions = TransactionModel.query.filter_by(client_id=user_id).all()
        
        if not transactions:
            return jsonify({"error": "No transactions found for this user"}), 404
        
        transactions_data = [{"transaction_id": t.id, "amount": t.amount, "date": t.date} for t in transactions]
        
        return jsonify({"transactions": transactions_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
