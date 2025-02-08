from flask import jsonify, request
from models.userModel import UserModel  # Correct import

def get_user(user_id):
    """Retrieve a user by ID."""
    try:
        user = UserModel.objects(id=user_id).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "user_id": str(user.id),
            "name": user.name,
            "income": user.income,
            "spending": user.spending
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_user():
    """Create a new user."""
    try:
        data = request.get_json()
        user = UserModel(**data)
        user.save_user()

        return jsonify({"message": "User created successfully", "user_id": str(user.id)}), 201

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

        return jsonify({
            "message": "User updated successfully",
            "updated_user": {
                "user_id": str(user.id),
                "income": user.income,
                "spending": user.spending
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
