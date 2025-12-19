"""
모델 학습 흐름 정의
(Logistic Regression → MLP 비교 실험)
"""

from preprocess import load_and_preprocess
from model import SentimentMLP

def train():
    X, y = load_and_preprocess("data/nsmc_sample.csv")

    # 실제 학습은 생략 (설계 중심 프로젝트)
    print("모델 학습 파이프라인 구성 완료")

if __name__ == "__main__":
    train()
