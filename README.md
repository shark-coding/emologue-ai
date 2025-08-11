# emologue-ai

## 🧵 프로젝트 설명
이 서버는 학습된 딥러닝 모델을 통해  `emologue`에서 전달 받은 사용자의 일기 데이터를 분석하고, 감정 분류 결과를 백엔드로 반환합니다. Flask/FastAPI 기반 REST API로 동작하며, 백엔드와 HTTP 통신을 통해 연동횝니다.

## 📁 프로젝트 구조
```
emologue-AI/
├── ai_model/
│   ├── __init__.py
│   ├── emotion_predictor.py           # (현재 미사용) 감정 예측 로직
│   └── predictor_server.py            # 현재 서비스에서 사용 중인 Flask 감정 분석 API 서버
│
├── Dictionary/                        # (현재 미사용) 사전 기반 감정 분석 모듈
│   ├── analyzer.py
│   ├── analyzer_server.py
│   ├── dictionary_analyzer.py
│   ├── tokenizer.py
│   └── data/
│       └── __init__.py
├── main.py                             # (현재 미사용)
└── README.md

```

## 🧰 기술 스택
- Python 3.12
- Flask
- Transformers(Hugging Face)

## ✨ 주요 기능
**1. 감정 분석 API**
- 입력: 텍스트
- 출력: 감정 레이블 및 확률

**2. 백엔드 연동**
- `emologue`의 분석 요청에 응답


## 📌 실행 방법
**1. 가상환경 생성 및 활성화**
- python -m venv venv
- source venv/bin/activate  # (Windows) venv\Scripts\activate

**2. 패키지 설치**
- pip install -r requirements.txt

**3. predictor_server.py 실행**
- 실행 파일이 있는 폴더로 이동한 뒤 아래 명령어 실행
- python predictor_server.py

