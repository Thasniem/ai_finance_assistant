from mongoengine import Document, StringField, FloatField

class UserModel(Document):
    meta = {'collection': 'users'}

    id = StringField(primary_key=True)  # ObjectId should be string
    name = StringField(required=True)
    income = FloatField(required=True)
    spending = FloatField(required=True)

    def save_user(self):
        """Save the user document."""
        super().save()

    def update_user(self, data):
        """Update user details."""
        self.update(**data)
        self.reload()
