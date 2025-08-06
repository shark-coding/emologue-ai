from Dictionary.dictionary_analyzer import DictionarySentimentAnalyzer

analyzer = DictionarySentimentAnalyzer()

text = input("일기 내용을 입력하세요: ")

result = analyzer.analyze(text)

print("분석 결과:")
print(f"- 전체 단어: {result['tokens']}")
print(f"- 일치 단어: {result['matched']}")
print(f"- 점수 합계: {result['final_score']}")
print(f"- 최종 감정: {result['sentiment']}")

# from ai_model.emotion_predictor import AIDeepSentimentAnalyzer
#
# analyzer = AIDeepSentimentAnalyzer()
#
# text = input("일기 내용을 입력하세요:\n")
# result = analyzer.analyze(text)
#
# print("\n[감정 분석 결과]")
# print(f"- 입력 문장: {result['text']}")
# print(f"- 예측 감정: {result['sentiment']} (score: {result['score']})")
# print(f"- 원본 레이블: {result['raw_label']}")