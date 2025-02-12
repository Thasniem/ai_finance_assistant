from flask import jsonify, request
from models.transactionModel import TransactionModel
from datetime import datetime

# Create a new transaction
def create_transaction(data):
    try:
        transaction = TransactionModel(
            client_id=data["client_id"],
            card_id=data["card_id"],
            amount = float(data["amount"].replace("$", "").strip()),  # Ensure no spaces
            date=data.get("date", datetime.utcnow()),
            use_chip=data.get("use_chip", ""),
            merchant_id=data.get("merchant_id"),
            merchant_city=data.get("merchant_city", ""),
            merchant_state=data.get("merchant_state", ""),
            zip_code=data.get("zip", ""),
            mcc=int(data["mcc"]),
            errors=data.get("errors", "").split(",") if data.get("errors") else []
        )
        transaction.save_transaction()
        return {"message": "Transaction created successfully!"}

    except Exception as e:
        return {"error": str(e)}

# Get transactions by user ID
def get_transactions(user_id):
    try:
        transactions = TransactionModel.get_transactions_by_user(user_id)
        return transactions if transactions else {"message": "No transactions found."}

    except Exception as e:
        return {"error": str(e)}

# Update a transaction by ID
def update_transaction(transaction_id, data):
    try:
        transaction = TransactionModel.objects(id=transaction_id).first()
        if not transaction:
            return {"error": "Transaction not found."}
        
        transaction.update_transaction(data)
        return {"message": "Transaction updated successfully!"}

    except Exception as e:
        return {"error": str(e)}
