# Movie Review Sentiment Analysis

NSMC 데이터를 활용한 PyTorch 기반 감성 분류 시스템

## Table of Contents

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
실제 텍스트 데이터에 적용해 보기 위해 시작되었습니다.

영화 리뷰와 같이 비정형적인 자연어 데이터에 대해
전통적인 머신러닝 모델과 신경망 모델이
어떻게 서로 다른 성능을 보이는지를 비교하고,
텍스트 분류 문제의 전체 처리 과정을 이해하는 것을 목표로 합니다.

이를 통해 이론으로 학습한 개념이
실제 데이터 분석 문제에서 어떻게 활용되는지를 확인하고자 합니다.

## 2. Data Acquisition

[Back to Table of Contents](#back-to-table-of-contents)

본 프로젝트에서는 **네이버 영화 리뷰 감성 데이터(NSMC)**를 사용하였습니다.

데이터의 주요 특징은 다음과 같습다.
- 약 20만 개의 한국어 영화 리뷰
- 각 리뷰는 감성 레이블을 가짐
      1: 긍정 리뷰
      0: 부정 리뷰

데이터는 CSV 형식으로 제공되며,
본 프로젝트에서는 전체 데이터 중 일부를 샘플링하여 실험에 활용하였습다.

Note: 데이터 크기 문제로 인해 GitHub에는 소량의 샘플 데이터만 포함되어 있습다.

## 3. Preprocessing

[Back to Table of Conte니다.
- 텍스트 데이터 전처리 과정의 중요성
- 기준 모델과 신경망 모델의 성능 차이
- 머신러닝 프로젝트의 전체 흐름에 대한 이해

이를 통해 수업에서 배운 이론과
실제 데이터 분석 문제 사이의 연결성을 명확히 확인할 수 있었습니다.

## 8. Technologies Used

[Back to Table of Contents](#back-to-table-of-contents)

Python

PyTorch

Scikit-learn

Pandas
