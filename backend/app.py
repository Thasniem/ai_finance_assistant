# app.py

from flask import Flask
from userRoutes import user_routes
from transactionRoutes import transaction_routes
from predictionRoutes import prediction_routes
from config import Config

app = Flask(__name__)

# Load configuration settings
app.config.from_object(Config)

# Register Blueprints
app.register_blueprint(user_routes)
app.register_blueprint(transaction_routes)
app.register_blueprint(prediction_routes)

if __name__ == "__main__":
    app.run(debug=True)
