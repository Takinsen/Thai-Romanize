import os
from pythainlp.corpus import download

# Set up data directory
data_path = "/tmp/pythainlp_data"
os.makedirs(data_path, exist_ok=True)
os.environ["PYTHAINLP_DATA_PATH"] = data_path

# Download required corpus files
print("Downloading required corpus files...")
download("thai_words")
download("thai_syllables")
print("Corpus files downloaded successfully.")