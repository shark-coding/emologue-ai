import sys
import os
import json

# tokenizer.py가 같은 폴더에 있다고 가정
from tokenizer import tokenize

def analyze(content, lexicon):
    tokens = tokenize(content)
    print("형태소:", tokens)

    score = 0.0
    for token in tokens:
        if token in lexicon:
            print(f"✔ 매칭됨: {token} → {lexicon[token]}")
            score += lexicon[token]
        else:
            print(f"✘ 매칭 안됨: {token}")

    if score > 0:
        sentiment = "긍정"
    elif score < 0:
        sentiment = "부정"
    else:
        sentiment = "중립"

    return {"final_score": score, "sentiment": sentiment}


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"emotionType": "NEUTRAL", "polarityScore": 0.0}, ensure_ascii=False))
        return

    content = " ".join(sys.argv[1:])

    lexicon_path = os.path.join(os.path.dirname(__file__), "data", "SentiWord_info.json")
    with open(lexicon_path, encoding='utf-8') as f:
        lexicon_data = json.load(f)

    # 사전을 딕셔너리로 구성하며 score를 float으로 변환
    lexicon = {}
    for entry in lexicon_data:
        word = entry.get("word")
        raw_score = entry.get("polarity", 0)

        try:
            score = float(raw_score)  # 문자열 점수 처리
        except (ValueError, TypeError):
            score = 0.0  # 변환 실패 시 기본값

        if word is not None:
            lexicon[word] = score

    result = analyze(content, lexicon)

    mapping = {
        "긍정": "POSITIVE",
        "부정": "NEGATIVE",
        "중립": "NEUTRAL"
    }
    emotion_type = mapping.get(result["sentiment"], "NEUTRAL")
    output = {
        "emotionType": emotion_type,
        "polarityScore": float(result["final_score"])
    }

    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
