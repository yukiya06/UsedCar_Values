# 중고차 판매 가격 예측 API 서비스
## 다중선형회귀 모델을 통한 가격 예측 및 APP 구현

* 데이터 분석 및 발표 : 안나 (Email: naan74532@gmail.com)
* 대시보드 [Metabase](https://usedcardashboards.herokuapp.com/public/dashboard/34de8990-8db3-4116-9301-5503336a8b71)
* 앱서비스 [중고차 가격예측](https://pjtappusedcar.herokuapp.com/)
* 전체 발표자료 [PDF](https://github.com/yukiya06/UsedCar_Values/blob/main/DA_%EC%95%88%EB%82%98_%EC%A4%91%EA%B3%A0%EC%B0%A8%ED%8C%90%EB%A7%A4%EA%B0%80%EA%B2%A9%EC%98%88%EC%B8%A1.pdf)

---
## 프로젝트 전체 목차
#### 1. 서론
  * 주제 선정 이유 및 데이터 특성
  * 데이터 파이프라인

#### 2.  탐색적 자료 분석 및 시각화 
  * 변수 상관 분석
  * 대시 보드 (Metabase)

#### 3. 중고차 판매가격 예측 ML 모델링

#### 4. API 유저 서비스 사용 프로세스

#### 5. 한계점 및 추후 발전방향

---
## 프로젝트 요약
### 1. 주제 선정 이유
* 다양한 정보를 활용하여 각각 개인에게 맞춤 서비스를 제공하는 것이 중요한 시대입니다. 머신 러닝을 활용하여 간단하면서도 필요한 정보를 제공 할 수 있도록 기획하였습니다.
* 고관여 제품(가격이 높고, 소비자들의 의사결정과정이나 정보처리과정이 복잡한 제품)인 자동차 가격을 예측하는 주제로 선정하여 머신 러닝의 활용 가치를 높였습니다.

### 2. 데이터 특성
* 중고차 데이터는 웹에서 수집하여 사용하므로 허위매물, 잘못된 정보 등을 검증하는 것이 중요합니다. 한국 데이터는 교차 검증 할 수 있는 자료가 유료인 경우가 많아 편의를 위해 미국사례로 선정하였습니다.
* 선정 데이터: https://www.kaggle.com/austinreese/craigslist-carstrucks-data
* Craigslist(크레이그리스트) https://craigslist.org/ : 중고 매물, 구인 구직, 주택, 자유 주제 토론등을 다루는 커뮤니티 웹사이트  
  미국내 중고차 매물 약 51만 건 스크레이핑 자료로 결측치, 중복데이터 제거 후 약 7만 건 사용  
  핵심정보 (주행거리, 등록번호 등) 이 누락된 정보가 많고, 다른 데이터로 대체 불가능하므로 제외하고 진행

### 3. 데이터 파이프라인
<img width="800" alt="데이터 파이프라인" src="https://user-images.githubusercontent.com/91524805/167399012-880b9e17-d17d-4a76-8b9d-6cee7d0c2828.png">

### 4. 중고차 판매가격 예측 ML 모델링 (다중선형 회귀)
<img width="800" alt="분석1" src="https://user-images.githubusercontent.com/91524805/167399797-fa3e18a1-1308-4f72-a807-6098a1b9ea15.png">

<img width="800" alt="분석2" src="https://user-images.githubusercontent.com/91524805/167399838-5eff6ca3-0a2a-4c03-8b87-5f112f5c94ca.png">

<img width="800" alt="분석3" src="https://user-images.githubusercontent.com/91524805/167399976-c567fdf1-a453-48c5-8fea-022049b7a8fe.png">

### 5. API 유저 서비스 사용 프로세스
<img width="820" alt="분석4" src="https://user-images.githubusercontent.com/91524805/167400071-428f1cdd-6d99-405d-8644-25eaccbca10e.png">

### 6. 한계점 및 추후 발전방향
* ML 모델 예측결과를  ①운행거리에 따른 판매가격 변화, ②연식에 따른 판매가격 변화의 그래프 2가지로 구현하고 싶었는데,  웹 페이지 구현이 어려워 간략히 결과 값만 출력하게 되어 아쉬웠습니다.

* ML모델(LinearRegression)을 활용한 서비스를 기획 했는데, 딥러닝을 활용하면 모델의 성능을 개선 할 수 있을 것 같습니다. 반응속도를 감안하여 결과를 비교해보면 더욱 좋을 것 같습니다.
---
### 7. 참고자료
* [회귀분석, 데이터 전처리](https://github.com/BAEintelli/U.S.A-usedcar-price_predict-project)
* [파이썬 객체 직렬화-Pickle](https://docs.python.org/ko/3/library/pickle.html?highlight=pickle)
* [다변인 선형회귀 모델 개발](https://ndb796.tistory.com/126?category=1013932)
* [플라스크 ML,DL RESTFul API](https://niceman.tistory.com/192)
* [플라스크 + scikit-learn models](https://towardsdatascience.com/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa)
* [웹 어플리케이션](https://github.com/AustinReese/UsedVehicleSearch)
