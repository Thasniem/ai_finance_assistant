import pandas as pd
import numpy as np
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from google_drive_downloader import GoogleDriveDownloader as gdd

# Define file paths
DATA_FOLDER = "data/"
MODEL_FOLDER = "backend/model/"

GOOGLE_DRIVE_LINKS = {
    "cards_data": "1gk9heV3AcrS95Vs9cj-lV6LUOMW_MwUd",
    "train_fraud_labels": "1VQltdmyAjpiYZQH1pyNc3M4rNoUDFrms",
    "mcc_codes": "1by6hstymC_HlK2lgjcDj_cXJNTGavFCi"
}

# Ensure directories exist
os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs(MODEL_FOLDER, exist_ok=True)

# Function to download files from Google Drive
def download_data():
    for name, file_id in GOOGLE_DRIVE_LINKS.items():
        file_path = os.path.join(DATA_FOLDER, f"{name}.xls")
        if not os.path.exists(file_path):
            print(f"Downloading {name}...")
            gdd.download_file_from_google_drive(file_id=file_id, dest_path=file_path, unzip=False)

# Load datasets
def load_data():
    download_data()

    users_df = pd.read_excel(os.path.join(DATA_FOLDER, "users_data.xls"))
    transactions_df = pd.read_excel(os.path.join(DATA_FOLDER, "transaction_data.xls"))
    cards_df = pd.read_excel(os.path.join(DATA_FOLDER, "cards_data.xls"))
    fraud_labels_df = pd.read_excel(os.path.join(DATA_FOLDER, "train_fraud_labels.xls"))
    mcc_df = pd.read_excel(os.path.join(DATA_FOLDER, "mcc_codes.xls"))
    
    return users_df, transactions_df, cards_df, fraud_labels_df, mcc_df

# Data Preprocessing
def preprocess_data(users_df, transactions_df, cards_df, fraud_labels_df):
    print("Fraud Labels Columns:", fraud_labels_df.columns)  # Debugging Step
    
    if "transaction_id" not in fraud_labels_df.columns:
        raise ValueError("Expected column 'transaction_id' missing in fraud_labels_df")

    # Merge transactions with fraud labels
    transactions_df = transactions_df.merge(
        fraud_labels_df, left_on="id", right_on="transaction_id", how="left"
    )
    
    # Convert categorical data to numeric
    transactions_df["errors"].fillna("No Error", inplace=True)
    transactions_df["errors"] = transactions_df["errors"].astype("category").cat.codes
    transactions_df["use_chip"] = transactions_df["use_chip"].astype("category").cat.codes

    # Handle missing financial values
    users_df["yearly_income"] = users_df["yearly_income"].replace(r"[\$,]", "", regex=True).fillna(0).astype(float)
    users_df["total_debt"] = users_df["total_debt"].replace(r"[\$,]", "", regex=True).fillna(0).astype(float)

    # Merge transactions with user data
    df = transactions_df.merge(users_df, left_on="client_id", right_on="id", how="left")

    # Define features and labels
    if "is_fraud" not in df.columns:
        raise ValueError("Column 'is_fraud' missing in fraud labels dataset")

    X = df[["amount", "errors", "use_chip", "yearly_income", "total_debt", "credit_score", "num_credit_cards"]]
    y = df["is_fraud"]

    return X, y

# Train the Model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Save model and scaler
    with open(os.path.join(MODEL_FOLDER, "finance_model.pkl"), "wb") as f:
        pickle.dump(model, f)
    
    with open(os.path.join(MODEL_FOLDER, "scaler.pkl"), "wb") as f:
        pickle.dump(scaler, f)

    print("Model training completed and saved!")

# Run training pipeline
if __name__ == "__main__":
    users_df, transactions_df, cards_df, fraud_labels_df, mcc_df = load_data()
    X, y = preprocess_data(users_df, transactions_df, cards_df, fraud_labels_df)
    train_model(X, y)
