# predictionModel.py

from mongoengine import Document, FloatField, IntField, StringField, DateTimeField
from datetime import datetime

class PredictionModel(Document):
    meta = {'collection': 'predictions'}

    # ID for each prediction entry
    id = IntField(required=True, unique=True)

    # The user's ID for whom the prediction is made
    user_id = IntField(required=True)

    # Prediction related data (e.g., predicted savings)
    predicted_savings = FloatField(required=True)
    predicted_expenses = FloatField()

    # Date and time when the prediction was made
    prediction_date = DateTimeField(default=datetime.utcnow)

    # Method to save the prediction document
    def save(self):
        self.save()

    # Method to update prediction details
    def update_prediction(self, data):
        self.update(**data)
        self.reload()
