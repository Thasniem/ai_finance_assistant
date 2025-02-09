#app.py
import os
from flask import Flask
from routes.userRoutes import user_routes  # Ensure this import is correct
from routes.transactionRoutes import transaction_routes
from routes.predictionRoutes import prediction_routes
from config import Config
from utils.data_loader import ensure_data_files

app = Flask(__name__)

# Load configuration settings
app.config.from_object(Config)

# Ensure datasets are downloaded before starting the server
ensure_data_files()

# Register Blueprints (Ensure module paths are correct)
app.register_blueprint(user_routes, url_prefix='/api')
app.register_blueprint(transaction_routes, url_prefix='/api')
app.register_blueprint(prediction_routes, url_prefix='/api')

@app.route("/")
def home():
    return "AI-Powered Personal Finance Assistant API is Running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render dynamically assigns a PORT
    app.run(host="0.0.0.0", port=port, debug=True)  # Enable debug mode
