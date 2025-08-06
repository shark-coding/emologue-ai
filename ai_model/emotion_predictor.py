from transformers import pipeline

class AIDeepSentimentAnalyzer:
    def __init__(self):
        self.model = pipeline("sentiment-analysis", model="WhitePeak/bert-base-cased-Korean-sentiment")

    def analyze(self, text: str):
        result = self.model(text)[0]
        label = result['label']
        score = result['score']

        if label == "LABEL_0":
            sentiment = "부정"
        elif label == "LABEL_1":
            sentiment = "긍정"
        else:
            sentiment = "중립"

        return {
            "text": text,
            "score": round(score, 4),
            "raw_label": label,
            "sentiment": sentiment
        }