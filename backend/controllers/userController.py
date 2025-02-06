# userController.py

from flask import jsonify, request
from .models.userModel import UserModel  # Assuming a MongoDB user model

# Route to get user details
def get_user(user_id):
    try:
        user = UserModel.query.filter_by(id=user_id).first()
        
        if user is None:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify({
            "user_id": user.id,
            "name": user.name,
            "income": user.income,
            "spending": user.spending
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to update user data (e.g., income or spending)
def update_user_data(user_id):
    try:
        data = request.get_json()
        
        user = UserModel.query.filter_by(id=user_id).first()
        
        if user is None:
            return jsonify({"error": "User not found"}), 404
        
        # Update user data
        user.income = data.get("income", user.income)
        user.spending = data.get("spending", user.spending)
        
        # Commit changes to the database
        user.save()
        
        return jsonify({
            "message": "User data updated successfully",
            "updated_user": {
                "user_id": user.id,
                "income": user.income,
                "spending": user.spending
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
