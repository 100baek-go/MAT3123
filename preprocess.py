"""
텍스트 전처리 모듈
- 결측치 제거
- 토큰화
- TF-IDF 벡터화
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def load_and_preprocess(path):
    df = pd.read_csv(path)
    df = df.dropna()

    texts = df['review']
    labels = df['label']

    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1,2)
    )
    X = vectorizer.fit_transform(texts)

    return X, labels
