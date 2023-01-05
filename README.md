# customs-notification-analysis-and-monitoring-system
글로벌 공급망 위기 대처를 위한, 세관 고시 분석 및 모니터링 시스템  
### <img src="https://user-images.githubusercontent.com/45115733/210746184-0fa89ee4-47b7-45cc-a9b3-c601c06ab846.png" width="25px" height="75%"/>Notice 
```
본 프로젝트는 Kotra 내부 서비스 적용을 위해 현재 계약을 진행하였고, 
코드를 포함한 최종 결과물의 사용 권한을 Kotra에 이관하였음을 알립니다.
그렇기에, 해당 repository에서는 회의록을 포함한 일부 작업만이 확인이 가능합니다.
```
## 기술 스택
> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">  
> <img src="https://img.shields.io/badge/selenium-6DB33F?style=for-the-badge&logo=selenium&logoColor=white">  
> <img src="https://img.shields.io/badge/sqlite3-00599C?style=for-the-badge&logo=sqlite&logoColor=white">    
> <img src="https://img.shields.io/badge/google%20cloud-F05032?style=for-the-badge&logo=google&logoColor=white">

<br>

## Collaborative organization
> <img src="https://user-images.githubusercontent.com/45115733/210560053-353dd44e-1442-4d00-8b92-c62ef2f4e621.png" width="100px" height="75%"/> **,**
> <img src="https://user-images.githubusercontent.com/45115733/210559728-81d83fb3-f73c-4757-8d4f-8f5f382de852.PNG" width="120px" height="75%"/>

1. **Kotra** (대한무역투자진흥공사) - 프로젝트 멘토링, 고도화 진행
2. **BigLeader** (빅리더) - 프로젝트 주관, 협조 진행

<br>

## 개발 멤버
+ **Team Leader**
  + [KwanJung98 (82KJ)](https://github.com/82KJ/) - FE / BE / Design Auto Scraper / NLP Model Selection & Application 
+ **Team Member**
  + [JangHyun Noh (NohJangHyun)](https://github.com/NohJangHyun) - Scraping (Japan) / Data Preprocessing / Testing & Results Analysis
  + [Yoona PARK (gyunnas)](https://github.com/gyunnas) - Scraping (America, Australia) / Data Preprocessing / BE
  + [JinSeo_Han (jinseoyaaa)](https://github.com/jinseoyaaa) - Scraping (Vietnam, China) / Data Preprocessing / Testing & Results Analysis

<br>
  
## 개요 
본 시스템은 2021년 10월경 발생한 **요소수 대란**과 같은 **글로벌 공급망 불안 사태를 예방**하기 위해 고안되었다.  
**해외 관세청 세관고시를 신속하게 파악**하여 산업 관계자에게 제공하는 것을 목표로 한다. 이를 위해, Kotra(대한무역투자진흥공사)와 연계하여 각종 해결책 및 시스템 구성 방식을 구상하였다.

+ 해외 관세청에 올라오는 세관 고시의 신속한 파악 --> 매일 고시를 크롤링하여 DB에 저장하는 **자동화 시스템** 구축  
+ 각 세관 고지가 어떠한 품목과 관련되어 있는지 분석 --> NLP 모델을 이용한 문서 **키워드 추출** 방식 적용
+ 각 세관 고지가 대한민국에 어떻게 영향을 줄 수 있는지 --> 자체 선정 **모니터링 품목** 매칭 및 **산업군 매칭표** 제공
+ 다양한 산업 관계자를 대상으로하는 서비스 제공 --> 사용자 친화적이고 직관적인 **웹 서비스** 구현

<br>

## Data Set
### 1. 5개국 세관고지 데이터
각 나라별 관세청 사이트의 업로드된 세관고시 수집 진행 (날짜, 제목, 링크, 내용, 영어 번역본, 한국어 번역본)
|국가|기간|개수|
|:---:|:---:|:---:|
|[중국](http://www.customs.gov.cn/customs/302249/302266/index.html)|1999.11.02~2022.07.25|2191개|
|[미국](https://www.cbp.gov/trade/rulings/bulletin-decisions)|2003.06.18~2022.07.26|937개|
|[일본](https://www.meti.go.jp/policy/external_economy/trade_control/wnlist.html)|2019.05.29~2022.08.01|500개|
|[호주](https://www.abf.gov.au/help-and-support/notices/australian-customs-notices)|2018.12.10~2022.08.23|1620개|
|[베트남](https://www.customs.gov.vn/index.jsp?pageId=4&cid=30)|2010.08.10~2022.07.01|1000개|

### 2. 모니터링 품목 데이터
대한민국과 각 나라별 교역 품목 기준으로 모니터링 품목 선정 및 수집 진행 (MTI, HSCODE, KSIC)
|국가|대분류|소분류|
|:---:|:---:|:---:|
|[중국](http://www.customs.gov.cn/customs/302249/302266/index.html)|100개|330개|
|[미국](https://www.cbp.gov/trade/rulings/bulletin-decisions)|100개|282개|
|[일본](https://www.meti.go.jp/policy/external_economy/trade_control/wnlist.html)|100개|274개|
|[호주](https://www.abf.gov.au/help-and-support/notices/australian-customs-notices)|100개|211개|
|[베트남](https://www.customs.gov.vn/index.jsp?pageId=4&cid=30)|100개|301개|

<br>

## NLP 모델 선정
### Sentence BERT - (all-mpnet-base-v2)
2018년 구글에서 공개한 Pretrained Model인 BERT를 미세 조정하여 **Sentence Embedding의 성능을 극대화**한 모델  
다양한 SBERT 모델 중, Sentence Embeddings과 Sematic Search의 평균 성능이 가장 뛰어난 all-mpnet-base-v2 선정  
미세 조정을 위해, **10억개의 문장 쌍 데이터로 contrastive learning**을 진행  
|Name|Avg Performance|Encoding Speed (sentences/sec)|Size (MB)|
|:---:|:---:|:---:|:---:|
|all-mpnet-base-v2|63.30|2800|420|

