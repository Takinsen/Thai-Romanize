import os

# Set writable path for PyThaiNLP
os.environ["PYTHAINLP_DATA_PATH"] = "/tmp/pythainlp_data"
os.makedirs("/tmp/pythainlp_data", exist_ok=True)

from app import app  # expose Flask app to Vercel
