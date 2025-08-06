from konlpy.tag import Okt
import re

okt = Okt()

def clean_text(text: str) -> str:
    text = re.sub(r"[^\uAC00-\uD7A3a-zA-Z\s]", "", text)  # 한글/영문/공백만 남김
    return text.strip()

def tokenize(text: str):
    cleaned = clean_text(text)
    tokens = [word for word, tag in okt.pos(cleaned, stem=True)]
    return tokens
