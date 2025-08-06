from flask import Flask, request, jsonify
from transformers import pipeline
# from flask_cors import CORS  # 필요 시 CORS 허용

app = Flask(__name__)
# CORS(app)  # CORS 허용 (Spring과 통신 시 필요할 수 있음)

# 모델 초기화
model = pipeline("sentiment-analysis", model="WhitePeak/bert-base-cased-Korean-sentiment")

@app.route('/predictor', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('content', '')

    if not text:
        return jsonify({"error": "No content provided"}), 400

    result = model(text)[0]
    label = result['label']
    score = result['score']

    if label == "LABEL_0":
        sentiment = "negative"
    elif label == "LABEL_1":
        sentiment = "positive"
    else:
        sentiment = "neutral"

    return jsonify({
        "emotionType": sentiment,
        "confidenceScore": round(score, 4)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
