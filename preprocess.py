"""
텍스트 전처리 모듈
- 결측치 제거
- 토큰화
- TF-IDF 벡터화
"""

import pandas as pd
import torch
from sklearn.feature_extraction.text import TfidfVectorizer

def load_and_preprocess(path, text_col="review", label_col="label"):
    df = pd.read_csv(path)
    df = df.dropna(subset=[text_col, label_col])

    texts = df[text_col].astype(str)
    labels = df[label_col].astype(int)

    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1,2)
    )
    X = vectorizer.fit_transform(texts)

    X = torch.from_numpy(X.toarray()).float()
    Y = torch.LongTensor(labels.values)

    return X, Y, vectorizer
