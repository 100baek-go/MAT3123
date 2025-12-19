"""
모델 학습 흐름 정의
(Logistic Regression → MLP 비교 실험)
"""
import torch
import torch.nn as nn
from preprocess import load_and_preprocess
from model import SentimentMLP

def train():
    X, y, vectorizer = load_and_preprocess("data/nsmc_sample.csv")
    print(f"입력 차원: {X.shape[1]}")
    
    # Logistic Regression
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X.numpy(), y.numpy())
    lr_acc = lr.score(X.numpy(), y.numpy())
    print(f"[Logistic Regression] Accuracy: {lr_acc:.4f}")

    # MLP 모델
    model = SentimentMLP(input_dim=X.shape[1])

    # 실제 학습은 생략 (설계 중심 프로젝트)
    print("[MLP] 모델 구조 정의 완료")
    print(model)
    print("모델 학습 파이프라인 구성 완료")

if __name__ == "__main__":
    train()
