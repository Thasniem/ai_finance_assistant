# config.py

import os

class Config:
    # Environment-specific configuration settings
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    # Database settings (adjust for your DB configuration)
    MONGO_URI = os.getenv('MONGO_URI', 'http://Thasniem:thfjd150@mycluster.0ivtg.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster')
    
    # Machine learning model path (in case you want to change the location)
    MODEL_PATH = os.getenv('MODEL_PATH', 'path_to_model/finance_predictor.pkl')
    
    # Optionally, you can add more config settings like logging, email, etc.
GOOGLE_DRIVE_LINKS = {
        "cards_data": "https://drive.google.com/uc?export=download&id=1gk9heV3AcrS95Vs9cj-lV6LUOMW_MwUd",
        "users_data": "https://drive.google.com/uc?export=download&id=1zFLQvs_8k4aUmrMfQRvnNZQ4H4jASE_w",
        "transactions_data": "https://drive.google.com/uc?export=download&id=12FegBfvchc5kUH9wCAkszTeepEn0QUcT",
        "train_fraud_labels": "https://drive.google.com/uc?export=download&id=1VQltdmyAjpiYZQH1pyNc3M4rNoUDFrms",
        "mcc_codes": "https://drive.google.com/uc?export=download&id=1by6hstymC_HlK2lgjcDj_cXJNTGavFCi"
    }
    DATA_DIR = os.path.join(os.path.dirname(__file__), "data")