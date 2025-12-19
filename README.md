# Movie Review Sentiment Analysis

NSMC 데이터를 활용한 PyTorch 기반 감성 분류 시스템

##Table of Contents

1. [Motivation](#motivation)

2. [Data Acquisition](#data-acquisition)

3. [Preprocessing](#preprocessing)

4. [Model](#model)

5. [Performance](#performance)

6. [Project Structure](#project-structure)

7. [Conclusion](#conclusion)

8. [Technologies Used](#technologies-used)

## 1. Motivation

[Back to Table of Contents](#back-to-table-of-contents)

본 프로젝트는 수업 시간에 배운 머신러닝 및 딥러닝 이론을
실제 텍스트 데이터에 적용해 보기 위해 시작되었다.

영화 리뷰와 같이 비정형적인 자연어 데이터에 대해
전통적인 머신러닝 모델과 신경망 모델이
어떻게 서로 다른 성능을 보이는지를 비교하고,
텍스트 분류 문제의 전체 처리 과정을 이해하는 것을 목표로 한다.

이를 통해 이론으로 학습한 개념이
실제 데이터 분석 문제에서 어떻게 활용되는지를 확인하고자 한다.

## 2. Data Acquisition

[Back to Table of Contents](#back-to-table-of-contents)

본 프로젝트에서는 **네이버 영화 리뷰 감성 데이터(NSMC)**를 사용하였다.

데이터의 주요 특징은 다음과 같다.

약 20만 개의 한국어 영화 리뷰

각 리뷰는 감성 레이블을 가짐

1: 긍정 리뷰

0: 부정 리뷰

데이터는 CSV 형식으로 제공되며,
본 프로젝트에서는 전체 데이터 중 일부를 샘플링하여 실험에 활용하였다.

Note: 데이터 크기 문제로 인해 GitHub에는 소량의 샘플 데이터만 포함되어 있다.

## 3. Preprocessing

[Back to Table of Contents](#back-to-table-of-contents)

텍스트 데이터를 모델에 입력하기 위해 다음과 같은 전처리 과정을 수행하였다.

Pandas를 이용한 데이터 로드

결측치 제거

TF-IDF 벡터화를 통한 텍스트의 수치화

어휘 수 제한을 통한 차원 축소

이를 통해 자연어 형태의 리뷰 데이터를
머신러닝 및 딥러닝 모델에서 처리 가능한 입력 형태로 변환하였다.

## 4. Model

[Back to Table of Contents](#back-to-table-of-contents)

본 프로젝트에서는 두 가지 모델을 사용하여 성능을 비교하였다.

Baseline Model

Logistic Regression

텍스트 분류 문제에서의 기본적인 기준 모델로 사용

이후 딥러닝 모델과의 성능 비교를 위한 기준선 역할

Deep Learning Model

PyTorch 기반 다층 퍼셉트론(MLP)

모델 구조는 다음과 같다.

입력층: TF-IDF 특징 벡터

은닉층: ReLU 활성화 함수

출력층: 2개 클래스(긍정 / 부정)

해당 모델은 수업에서 다룬 신경망 개념을 반영하여 설계되었다.

## 5. Performance

[Back to Table of Contents](#back-to-table-of-contents)

모델의 성능은 정확도를 기준으로 비교하였다.

모델	정확도
Logistic Regression	약 83%
PyTorch MLP	약 86%

실험 결과, MLP 모델이 기준 모델보다 더 높은 정확도를 보였다.
이는 텍스트 데이터의 비선형적인 특성을 신경망이 효과적으로 학습했기 때문으로 해석할 수 있다.

또한 Confusion Matrix 분석을 통해
약한 부정 표현이 포함된 리뷰에서 오분류가 상대적으로 많이 발생함을 확인하였다.

본 프로젝트는 정량적 성능 향상뿐만 아니라
모델 간 특성 차이를 이해하는 데 의의를 둔다.

## 6. Project Structure

[Back to Table of Contents](#back-to-table-of-contents)

bash
  .
  ├── preprocess.py   # 텍스트 전처리 및 벡터화
  ├── model.py        # PyTorch MLP 모델 정의
  ├── train.py        # 모델 학습 파이프라인
  ├── README.md
  └── data/
      └── nsmc_sample.csv

## 7. Conclusion

[Back to Table of Contents](#back-to-table-of-contents)

본 프로젝트를 통해 다음과 같은 점을 학습할 수 있었다.

텍스트 데이터 전처리 과정의 중요성

기준 모델과 신경망 모델의 성능 차이

머신러닝 프로젝트의 전체 흐름에 대한 이해

이를 통해 수업에서 배운 이론과
실제 데이터 분석 문제 사이의 연결성을 명확히 확인할 수 있었다.

## 8. Technologies Used

[Back to Table of Contents](#back-to-table-of-contents)

Python

PyTorch

Scikit-learn

Pandas
