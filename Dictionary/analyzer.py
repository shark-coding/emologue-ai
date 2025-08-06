import json
from Dictionary.tokenizer import tokenize

class DictionarySentimentAnalyzer:
    def __init__(self, lexicon_path="data/SentiWord_info.json"):
        with open(lexicon_path, 'r', encoding='utf-8') as f:
            senti_data = json.load(f)
        self.lexicon = {entry['word']: int(entry['polarity']) for entry in senti_data}

    def analyze(self, text: str):
        tokens = tokenize(text)
        score = 0
        matched = []

        for token in tokens:
            if token in self.lexicon:
                polarity = self.lexicon[token]
                score += polarity
                matched.append((token, polarity))

        return {
            "tokens": tokens,
            "matched": matched,
            "final_score": score,
            "sentiment": self._score_to_sentiment(score)
        }

    def _score_to_sentiment(self, score: int) -> str:
        if score > 0:
            return "긍정"
        elif score < 0:
            return "부정"
        else:
            return "중립"