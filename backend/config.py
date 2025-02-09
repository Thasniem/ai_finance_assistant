#config.py
import os

class Config:
    # Enable debug mode for development
    DEBUG = os.getenv('DEBUG', 'True') == 'True'  

    # Security settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    # Use environment variable for MongoDB URI (Avoid Hardcoding!)
    MONGO_URI = os.getenv('MONGO_URI')

    # Machine Learning Model Path (ensure model exists)
    MODEL_PATH = os.getenv('MODEL_PATH', os.path.join(os.getcwd(), 'models/finance_predictor.pkl'))

    # Create a proper data directory (absolute path)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get base directory
    DATA_DIR = os.path.join(BASE_DIR, "data")  
    os.makedirs(DATA_DIR, exist_ok=True)  # Ensure the folder exists

    # Google Drive Dataset Links (Use `gdown` for secure download)
    GOOGLE_DRIVE_LINKS = {
        "cards_data": "1gk9heV3AcrS95Vs9cj-lV6LUOMW_MwUd",
        "train_fraud_labels": "1VQltdmyAjpiYZQH1pyNc3M4rNoUDFrms",
        "mcc_codes": "1by6hstymC_HlK2lgjcDj_cXJNTGavFCi"
    }

    # MongoDB Collections
    MONGO_COLLECTIONS = {
        "transactions": "transactions_data",
        "users": "users_data"
    }
