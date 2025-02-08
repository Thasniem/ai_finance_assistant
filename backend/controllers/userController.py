from flask import jsonify, request
from models.userModel import UserModel

def get_user(user_id):
    """Retrieve a user by ID."""
    try:
        user = UserModel.objects(id=user_id).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify(user.to_mongo().to_dict()), 200  # Return full user object

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_user():
    """Create a new user."""
    try:
        data = request.get_json()

        # Convert numeric fields properly
        data["id"] = int(data["id"])
        data["current_age"] = int(data["current_age"])
        data["retirement_age"] = int(data["retirement_age"])
        data["birth_year"] = int(data["birth_year"])
        data["birth_month"] = int(data["birth_month"])
        data["latitude"] = float(data["latitude"])
        data["longitude"] = float(data["longitude"])
        data["credit_score"] = int(data["credit_score"])
        data["num_credit_cards"] = int(data["num_credit_cards"])

        # Store per_capita_income, yearly_income, and total_debt as raw strings (with "$")
        user = UserModel(**data)
        user.save_user()

        return jsonify({"message": "User created successfully", "user_id": user.id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_user(user_id):
    """Update user details."""
    try:
        data = request.get_json()
        user = UserModel.objects(id=user_id).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        user.update_user(data)

        return jsonify({"message": "User updated successfully", "user_id": user.id}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
