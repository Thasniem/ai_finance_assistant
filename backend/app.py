from flask import Flask
from routes.userRoutes import user_routes
from routes.transactionRoutes import transaction_routes
from routes.predictionRoutes import prediction_routes
from config import Config
from utils.data_loader import ensure_data_files  # Import dataset loader

app = Flask(__name__)

# Load configuration settings
app.config.from_object(Config)

# Ensure datasets are available
ensure_data_files()

# Register Blueprints
app.register_blueprint(user_routes, url_prefix='/api')
app.register_blueprint(transaction_routes, url_prefix='/api')
app.register_blueprint(prediction_routes, url_prefix='/api')

@app.route("/")
def home():
    return "AI-Powered Personal Finance Assistant API is Running!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT dynamically
    app.run(host="0.0.0.0", port=port, debug=True)
