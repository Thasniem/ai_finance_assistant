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

# Ensure datasets are available
ensure_data_files()
@app.route("/")
def home():
    return "AI-Powered Personal Finance Assistant API is Running!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT dynamically
    app.run(host="0.0.0.0", port=port)

 