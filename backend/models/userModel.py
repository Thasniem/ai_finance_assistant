#userModel.py
from mongoengine import Document, StringField, IntField, FloatField

class UserModel(Document):
    """User model schema for MongoDB."""
    meta = {'collection': 'users'}

    id = IntField(primary_key=True, required=True)
    current_age = IntField(required=True)
    retirement_age = IntField(required=True)
    birth_year = IntField(required=True)
    birth_month = IntField(required=True)
    gender = StringField(required=True)
    address = StringField(required=True)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    per_capita_income = StringField(required=True)  # Keeping as string since it contains "$"
    yearly_income = StringField(required=True)
    total_debt = StringField(required=True)
    credit_score = IntField(required=True)
    num_credit_cards = IntField(required=True)

    def save_user(self):
        """Save user instance to the database."""
        self.save()

    def update_user(self, data):
        """Update user details with given data."""
        self.update(**data)
        self.reload()
