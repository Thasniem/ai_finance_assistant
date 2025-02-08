import os

class Config:
    # Environment-specific configuration settings
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    # Database settings (MongoDB Atlas connection string)
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://Thasniem:thfjd150@mycluster.0ivtg.mongodb.net/finance_assistant_db?retryWrites=true&w=majority')

    # Machine learning model path (adjust for your model location)
    MODEL_PATH = os.getenv('MODEL_PATH', 'models/finance_predictor.pkl')

    # Directory for storing downloaded datasets
    DATA_DIR = os.path.abspath("data")

    # Google Drive dataset links
    GOOGLE_DRIVE_LINKS = {
        "cards_data": "https://drive.google.com/uc?export=download&id=1gk9heV3AcrS95Vs9cj-lV6LUOMW_MwUd",
        "users_data": "https://drive.google.com/uc?export=download&id=1zFLQvs_8k4aUmrMfQRvnNZQ4H4jASE_w",
        "transactions_data": "https://drive.google.com/uc?export=download&id=12FegBfvchc5kUH9wCAkszTeepEn0QUcT",
        "train_fraud_labels": "https://drive.google.com/uc?export=download&id=1VQltdmyAjpiYZQH1pyNc3M4rNoUDFrms",
        "mcc_codes": "https://drive.google.com/uc?export=download&id=1by6hstymC_HlK2lgjcDj_cXJNTGavFCi"
    }
