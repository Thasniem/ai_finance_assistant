import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Define paths for data (Update if needed)
TRANSACTIONS_PATH = "backend/data/transactions_data.xlsx"
USERS_PATH = "backend/data/users_data.xlsx"
MODEL_DIR = "backend/model"

# Ensure the model directory exists
os.makedirs(MODEL_DIR, exist_ok=True)

# Function to clean currency values
def clean_currency(value):
    """Convert currency values (e.g., '$77.00') to float."""
    if isinstance(value, str):
        return float(value.replace("$", "").replace(",", ""))
    return value

# Load transaction data
transactions = pd.read_excel(TRANSACTIONS_PATH)
transactions["amount"] = transactions["amount"].apply(clean_currency)

# Load user data
users = pd.read_excel(USERS_PATH)
users["yearly_income"] = users["yearly_income"].apply(clean_currency)
users["per_capita_income"] = users["per_capita_income"].apply(clean_currency)
users["total_debt"] = users["total_debt"].apply(clean_currency)

# Merge transactions with user data based on client_id
data = transactions.merge(users, left_on="client_id", right_on="id")

# Feature Selection (Choose meaningful features)
features = [
    "amount", "use_chip", "merchant_id", "zip", "credit_score",
    "yearly_income", "total_debt", "num_credit_cards"
]
target = "savings_prediction"  # Adjust this based on your goal

# Drop missing values
data = data.dropna(subset=features)

# Encode categorical variables (use_chip)
label_encoder = LabelEncoder()
data["use_chip"] = label_encoder.fit_transform(data["use_chip"])

# Split into features (X) and target (y)
X = data[features]
y = np.random.randint(500, 5000, size=len(X))  # Generate dummy target for now

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save model and scaler
joblib.dump(model, os.path.join(MODEL_DIR, "finance_model.pkl"))
joblib.dump(scaler, os.path.join(MODEL_DIR, "scaler.pkl"))

print("Model and scaler saved successfully!")
