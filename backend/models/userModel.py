from mongoengine import Document, StringField, IntField, FloatField

class UserModel(Document):
    """User model schema for MongoDB."""
    meta = {'collection': 'users'}

    # User Information
    id = IntField(primary_key=True, required=True)
    current_age = IntField(required=True)
    retirement_age = IntField(required=True)
    birth_year = IntField(required=True)
    birth_month = IntField(required=True)
    gender = StringField(required=True)
    address = StringField(required=True)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)

    # Financial Data
    per_capita_income = StringField(required=True)  # Keeping as string due to "$"
    yearly_income = StringField(required=True)
    total_debt = StringField(required=True)
    credit_score = IntField(required=True)
    num_credit_cards = IntField(required=True)

    def save_user(self):
        try:
            self.save()
        except Exception as e:
            raise Exception(f"Database Error: {str(e)}")
    @classmethod
    def get_user_by_id(cls, user_id):
        """Fetch user by ID."""
        user = cls.objects(id=user_id).first()
        return user.to_mongo().to_dict() if user else None

    def update_user(self, data):
        """Update user details with given data."""
        self.modify(**data)
        self.reload()
