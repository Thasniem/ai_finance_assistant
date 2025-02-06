# config.py

import os

class Config:
    # Environment-specific configuration settings
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    # Database settings (adjust for your DB configuration)
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/finance')
    
    # Machine learning model path (in case you want to change the location)
    MODEL_PATH = os.getenv('MODEL_PATH', 'path_to_model/finance_predictor.pkl')
    
    # Optionally, you can add more config settings like logging, email, etc.
