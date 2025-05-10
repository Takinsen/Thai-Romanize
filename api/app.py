import os

# Set a custom path for pythainlp data, using Vercel's writable /tmp directory
os.environ["PYTHAINLP_DATA_PATH"] = "/tmp/pythainlp_data"

from flask import Flask, request, jsonify
from pythainlp.transliterate import romanize
from pythainlp.tokenize import word_tokenize

app = Flask(__name__)

@app.route("/romanize", methods=["GET"])
def romanize_thai():
    try:
        text = request.args.get("text")
        if not text:
            return jsonify({"error": "Missing 'text' parameter"}), 400

        words = word_tokenize(text)
        romanized_words = [romanize(word, engine="thai2rom") for word in words]
        romanized_text = " ".join(romanized_words)

        return jsonify({"romanized": romanized_text})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
