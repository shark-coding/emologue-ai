from flask import Flask, request, jsonify
from tokenizer import tokenize
import json
import os

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    content = data.get('content', '')

    lexicon_path = os.path.join(os.path.dirname(__file__), "data", "SentiWord_info.json")
    with open(lexicon_path, encoding='utf-8') as f:
        lexicon_data = json.load(f)

    lexicon = {}
    for entry in lexicon_data:
        word = entry.get("word")
        raw_score = entry.get("polarity", 0)
        try:
            score = float(raw_score)
        except (ValueError, TypeError):
            score = 0.0
        if word is not None:
            lexicon[word] = score

    tokens = tokenize(content)
    score = sum(lexicon.get(token, 0.0) for token in tokens)

    if score > 0:
        sentiment = "POSITIVE"
    elif score < 0:
        sentiment = "NEGATIVE"
    else:
        sentiment = "NEUTRAL"

    return jsonify({
        "emotionType": sentiment,
        "polarityScore": score
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
