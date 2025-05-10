import os

# Set this BEFORE importing anything from PyThaiNLP
os.environ["PYTHAINLP_DATA_PATH"] = "/tmp/pythainlp_data"
os.makedirs("/tmp/pythainlp_data", exist_ok=True)

# Now delegate to your actual app
import app  # This runs app.py
