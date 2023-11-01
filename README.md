# Multi-Telecom
고객 특성에 따른 이탈 및 요금 분석과 예측을 기반으로 한 통신사 해지율 개선 마케팅 서비스
<br>
<br>

## 프로젝트 설명
- 언어 : python, google colab, jupyter lab
- 개발 환경 : Google Cloud Project (GCP), Looker studio, BigQuery, Django
- 인원 : 5명 (팀장 : [shinyeop hwang](https://github.com/HSYhrae), 팀원 4명)
- 기간 : 2023.10.26 - 2023.12.05
- 주요내용
  + 통신사 고객 이탈에 대한 예측 및 요금에 따른 통신사의 매출 예측을 기반으로 함.
  + 최종적으로 이탈율이 높은 노령층을 타겟층으로 삼아 마케팅 서비스 제안을 목표로 함.
  + 대시보드의 경우 Looker studio를 기반으로 깔끔한 버전의 제작을 목표로 함.
  + 웹 배포의 경우 Django를 사용해서 Looker studio 대시보드와는 차별성을 두려함.
 
- 역할
  + 팀원들이 희망하는 진로에 따라 역할을 분담함.
    + 데이터 분석 : [shinyeop hwang](https://github.com/HSYhrae), HaJeong-K(본인)
    + 대시보드 제작 및 마케팅 관련 : [Sohyeon Choi](https://github.com/Sohyeon-Choi), [Sumin Choi](https://github.com/sumin0308)
    + 웹 배포 : [Dongwon_Choi](https://github.com/DongWonC)
   
- 데이터
  + 데이터는 캐글 데이터 셋 [Telco Customer Churn](https://www.kaggle.com/datasets/sibelius5/telco-customer-churn?select=Telco_customer_churn_cleaned.csv) 을 사용함.
  + 국내, 해외 모두 통신사 관련 데이터는 존재하지 않아 가상의 데이터 셋을 사용함.
 
<br>

## 주제 변천사
### 선택한 대주제 : 통신사 고객 데이터 분석과 해지율 개선 및 마케팅 서비스
<br>

1. 통신사 데이터 셋을 IBM 데이터 셋으로 정함.
<br>

2. 1차 마케팅에 대한 방향성 토론.
   + B2B / B2C 방향성 토론 => B2C 선택
     + 기업간의 마케팅을 대상으로 하려면 추가적으로 데이터 셋을 구해야하는데 데이터를 구할 방법이 없음.
<br>

3. 2차 마케팅에 대한 방향성 토론.
   + 전반적인 마케팅 방안 보다 타겟층을 두고 마케팅을 하는 의견.
     + EDA를 기반으로 연령대로 분석한 부분에서 노령층의 이탈율이 높은 확실한 특징을 보이고 있어서 노령층을 타겟팅함.
    
<br>

## 목표

- 분석의 경우 예측을 중점으로 두고 2가지 예측을 진행함.
  + 고객 이탈에 대한 예측을 중심으로 하며, 추가적으로 고객 특성에 대한 요금을 기반으로 한 통신사 매출에 대한 예측을 진행함.
  + 고객 이탈 예측의 경우 다양한 머신러닝을 사용해서 비교하는 것을 목표로 함.
  + 통신사 매출에 대한 예측의 경우 폭넓은 머신러닝보단 평가지표가 높아지는 것을 목표로 함.
 <br>
 
- 대시보드
  + Looker studio를 사용해서 시각화 기반의 대시보드를 제작하는 것을 목표로 함.
  + 최대한 많은 내용을 담기 보다는 핵심만을 담아 깔끔하게 정리하는 것을 목표로 함.
 <br>
 
- 웹 배포
  + Django를 기반으로 Looker studio 대시보드와는 다르게 원 데이터부터 예측된 데이터까지의 내용을 담아 마케팅에 대한 제안 및 최종 분석 결과 전달을 목표로 함.
  + 분석의 내용을 중점으로 배포하기보단, 분석의 내용을 기반으로 제안되는 마케팅 서비스에 대해 배포함.
 
<br>

## 개발 로그 기록
- 레포 생성일자를 기준으로 작성됨.(23.10.31)
<br>

[2023.10.31]
- 오늘 한 일
  + 데이터 분석 : 데이터 전처리, EDA, 머신러닝 관련 코드 작업 + 빅쿼리 추가 연동.
  + 대시보드 : Looker studio 제작을 위한 심화 공부. (및 추가 마케터 프로젝트로 광고 제작 진행.)
  + 웹 배포 : Django 관련 틀 제작.
 
- 오늘 못한 일
  + 데이터 분석 : 데이터 EDA 마무리.
  + 기획 발표 준비 : ppt 1차 정리.
 
- 내일 할 일
  + 데이터 분석 : 데이터 EDA 마무리 및 머신러닝 1차 구체화.
  + 대시보드 : Looker studio 제작을 위한 심화 공부 및 제작 준비.
  + 웹 배포 : Django 관련 틀 제작.
  + 기획 발표 준비 : ppt 1차 정리.
 <br>
 
[2023.11.01]
- 오늘 한 일
  + 데이터 분석 : 통신사 데이터 전처리 및 EDA 완료.
  + 대시보드 : 마케팅 관련 자료 수집. (및 추가 마케터 프로젝트로 광고 노출수 증가를 위한 공부.)
  + 웹 배포 : Django 복습.
  + 기획 발표 준비 : ppt 1차 정리.
 
- 오늘 못한 일
  + 데이터 분석 : 고객 이탈 머신러닝 코드 초안 작성.
  + 대시보드 : Looker studio 제작을 위한 심화 공부.
  + 웹 배포 : 대시보드 UI 구상.
  + 기획 발표 준비 : ppt 1차 마무리.
 
- 내일 할 일
  + 데이터 분석 : 노령층 데이터로만 추가 EDA 수행, 고객 이탈 머신러닝 코드 초안 작성.
  + 대시보드 : Looker studio 제작을 위한 심화 공부 및 제작 준비.
  + 웹 배포 : Django 복습 및 대시보드 UI 구상.
  + 기획 발표 준비 : ppt 2차 정리.
