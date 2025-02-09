from mongoengine import Document, IntField, FloatField, StringField, DateTimeField, ListField
from datetime import datetime

class TransactionModel(Document):
    meta = {'collection': 'transactions'}

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
    def save_transaction(self):
        self.save()

    # Method to fetch transactions by user_id
    @classmethod
    def get_transactions_by_user(cls, user_id):
        transactions = cls.objects(client_id=user_id).order_by('-date')
        return [t.to_mongo().to_dict() for t in transactions] if transactions else []

    # Method to update transaction details
    def update_transaction(self, data):
        self.modify(**data)
        self.reload()
