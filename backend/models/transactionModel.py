# transactionModel.py

from mongoengine import Document, IntField, FloatField, StringField, DateTimeField, ListField
from datetime import datetime

class TransactionModel(Document):
    meta = {'collection': 'transactions'}

    # Transaction ID
    id = IntField(required=True, unique=True)

    # Client ID associated with this transaction
    client_id = IntField(required=True)

    # Card ID used for this transaction
    card_id = IntField(required=True)

    # Amount of the transaction
    amount = FloatField(required=True)

    # Date and time of the transaction
    date = DateTimeField(default=datetime.utcnow)

    # Information about how the transaction was made (e.g., swipe, chip, etc.)
    use_chip = StringField()

    # Merchant details
    merchant_id = IntField()
    merchant_city = StringField()
    merchant_state = StringField()
    zip_code = StringField()

    # Merchant Category Code (MCC) for the transaction
    mcc = IntField()

    # Any errors that occurred during the transaction
    errors = ListField(StringField())

    # Method to save the transaction document
    def save(self):
        self.save()

    # Method to update transaction details
    def update_transaction(self, data):
        self.update(**data)
        self.reload()
