from mongoengine import Document, FloatField, IntField, DateTimeField
from datetime import datetime

class PredictionModel(Document):
    meta = {'collection': 'predictions'}

    # The user's ID for whom the prediction is made
    user_id = IntField(required=True)

    # Prediction related data
    income = FloatField(required=True)
    spending = FloatField(required=True)
    predicted_savings = FloatField(required=True)
    
    # Optional: Add predicted_expenses if needed
    predicted_expenses = FloatField(default=0.0)

    # Date and time when the prediction was made
    prediction_date = DateTimeField(default=datetime.utcnow)

    # Method to save the prediction document
    def save_prediction(self):
        self.save()

    # Method to fetch prediction by user_id
    @classmethod
    def get_prediction_by_user(cls, user_id):
        prediction = cls.objects(user_id=user_id).order_by('-prediction_date').first()
        return prediction.to_mongo().to_dict() if prediction else None

    # Method to update prediction details
    def update_prediction(self, data):
        self.modify(**data)
        self.reload()
