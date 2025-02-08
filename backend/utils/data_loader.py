import os
import requests
from config import Config

def download_file(url, save_path):
    """Download dataset from Google Drive and save it locally."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download: {url}")

def ensure_data_files():
    """Ensure all required datasets are downloaded."""
    os.makedirs(Config.DATA_DIR, exist_ok=True)
    
    for file_name, url in Config.GOOGLE_DRIVE_LINKS.items():
        file_path = os.path.join(Config.DATA_DIR, f"{file_name}.csv" if "json" not in file_name else f"{file_name}.json")
        if not os.path.exists(file_path):
            download_file(url, file_path)
        else:
            print(f"Dataset exists: {file_path}")

if __name__ == "__main__":
    ensure_data_files()
