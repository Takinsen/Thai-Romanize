from flask import Flask, request, jsonify
from pythainlp.transliterate import romanize
import deepcut

app = Flask(__name__)

@app.route("/romanize", methods=["GET"])
def romanize_thai():
    text = request.args.get("text")  # Get ?text=... from query string
    if not text:
        return jsonify({"error": "Missing 'text' parameter"}), 400

    words = deepcut.tokenize(text)
    romanized_words = [romanize(word, engine="thai2rom") for word in words]
    romanized_text = " ".join(romanized_words)

    return jsonify({"romanized": romanized_text})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
