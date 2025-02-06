# userModel.py

from mongoengine import Document, StringField, IntField, FloatField, ListField

class UserModel(Document):
    meta = {'collection': 'users'}

    # User's ID (could be generated or used from an external system)
    id = IntField(required=True, unique=True)
    
    # User's name
    name = StringField(required=True)

    # Financial data
    income = FloatField(required=True)
    spending = FloatField(required=True)
    
    # Additional user details
    birth_year = IntField()
    birth_month = IntField()
    gender = StringField()
    address = StringField()
    latitude = FloatField()
    longitude = FloatField()
    credit_score = IntField()
    num_credit_cards = IntField()

    # Method to save the user document
    def save(self):
        self.save()

    # Method to update user details
    def update_user(self, data):
        self.update(**data)
        self.reload()

