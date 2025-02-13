from flask import jsonify, request
from backend.models.userModel import UserModel

def get_user(user_id):
    """Retrieve a user by ID."""
    try:
        user = UserModel.get_user_by_id(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user), 200

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

        # Convert financial fields (remove "$" and store as float)
        data["per_capita_income"] = float(data["per_capita_income"].replace("$", "").replace(",", ""))
        data["yearly_income"] = float(data["yearly_income"].replace("$", "").replace(",", ""))
        data["total_debt"] = float(data["total_debt"].replace("$", "").replace(",", ""))

        user = UserModel(**data)
        user.save_user()

        return jsonify({"message": "User created successfully", "user_id": user.id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_user(user_id):
    """Update user details and return updated user info."""
    try:
        data = request.get_json()
        user = UserModel.objects(id=user_id).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        updated_user = user.update_user(data)  # Modified function now returns updated user

        return jsonify({"message": "User updated successfully", "updated_user": updated_user}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

