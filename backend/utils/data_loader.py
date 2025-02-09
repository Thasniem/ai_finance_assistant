#data_loader.py
import os
import requests
from config import Config

def download_file(url, save_path):
    """Download dataset from Google Drive and save it locally."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for HTTP failures (e.g., 404, 403)

        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f" Downloaded: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f" Failed to download {url}: {e}")

def ensure_data_files():
    """Ensure all required datasets are downloaded."""
    os.makedirs(Config.DATA_DIR, exist_ok=True)

    for file_name, url in Config.GOOGLE_DRIVE_LINKS.items():
        file_ext = ".json" if url.endswith(".json") else ".csv"  # Detect file type
        file_path = os.path.join(Config.DATA_DIR, f"{file_name}{file_ext}")

        if not os.path.exists(file_path):
            print(f"⬇ Downloading {file_name}...")
            download_file(url, file_path)
        else:
            print(f" Dataset already exists: {file_path}")

if __name__ == "__main__":
    ensure_data_files()
