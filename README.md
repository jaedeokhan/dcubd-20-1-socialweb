# SocialWebMining
## 2020 1학기 python으로 네이버 뉴스 크롤링해서 pymysql에 데이터를 저장한 후 군집화, LDA 토픽 모델링

### 1. 환경 설정
1. Ec2 Ubuntu 18.04 에서 mysql server install, bind-address config[install-config-mysql.md](https://github.com/jaedeokhan/ducbd-20-1-socialweb/blob/master/mdfile/install-config-mysql.md)
2. Pymysql 사용법 [use-pymysql.md](https://github.com/jaedeokhan/ducbd-20-1-socialweb/blob/master/mdfile/use-pymysql.md)
   * Form 입력 양식 태그와 구조화 태그 [4_form.md](https://github.com/jaedeokhan/SocialWebMining/blob/master/mdfile/4_form.md)
4. Crawling sibling 내용 정리 [sibling.md](https://github.com/jaedeokhan/SocialWebMining/blob/master/mdfile/sibling.md)
5. 위의 1번, 네이버 뉴스 크롤링, pymysql 사용법, .save data, .save file, K-Mean 군집 분석 [0605_pymysql.use.md](https://github.com/jaedeokhan/SocialWebMining/blob/master/mdfile/0605_pymysql_use.md)

### 2. Crawlig 진행
1. 0417 FRI 크롤링 기초 - 영어 교육 사이트 데이터 가져오기, 대구가톨릭 데이터 가져오기 [0417Fri_Crawling.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0417Fri_Crawling.ipynb)
2. 0422 WED 네이버 댓글 크롤링 [0422_wed.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0422_wed.ipynb)
3. 0424 FRI 네이버 뉴스 크롤링 진행, pymysql 모듈을 사용해서 mysql에 데이터 삽입 [0424_fri_naver_news_address.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0424_fri_naver_news_address.ipynb)
4. 0508 FRI 네이버 뉴스 크롤링 palceholder 방식 사용, pymysql로 데이터를 SELECT해서 딕셔너리안에 리스트로 저장 , .csv 파일로 저장 [0508Fri_naver_news_crawling.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0508Fri_naver_news_crawling.ipynb)
5. 0513 WED 정규 표현식 문법 [0513_1_regular_expression.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0513_1_regular_expression.ipynb)
6. 0513 WED 사전 처리 - corpus(말뭉치), 불용어 제거(nltk 패키지 이용), N-gram 사용 [0513_2_dictionary_corpus.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0513_2_dictionary_corpus.ipynb)
7. 0513 WED 품사 분석 - Part-Of-Speech(POS 태깅), KoNLPy 패키지를 사용, Hannanum 사용 [0513_3_part_of_speech.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0513_3_part_of_speech.ipynb)
8. 0515 FRI k - 평균 군집화 수행 - [0514_2_cluster.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0514_2_cluster.ipynb)
9. 0515 FRI 단어 빈도수 체크, 문재인 대통령, 트럼프취임 연설문 워드 클라우드 - [0514_word_frequency.ipynb
](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0514_word_frequency.ipynb)
10. 0520 WED TF(Term Frequency), IDF, K-MEAN 군집 분석 - [0520_clstuer_analysis.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0520_clstuer_analysis.ipynb)
11. 0521 FRI 네이버 뉴스 크롤링으로 유한양행, 라돈, 삼성전자 데이터 가져와서 .csv 파일로 만들고 K-MEAN 군집화 수행 - [0521fri_news_clustering.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0521fri_news_clustering.ipynb)
12. 0610 WED K-대푯값 군집 분석 - [0610wed_k-대푯값.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0610wed_k-%EB%8C%80%ED%91%AF%EA%B0%92.ipynb)
13. 0612 FRI LDA(Latent Dirichlet Allocaiton) 토픽 모델링 - [0612FRI_토픽모델링.ipynb](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0612FRI_%ED%86%A0%ED%94%BD%EB%AA%A8%EB%8D%B8%EB%A7%81.ipynb)
14. 0619 FRI 크롤링한 csv 파일을 이용해서 train/test dataset을 나눠서 LDA 토픽 모델링 - [0617WED_수집데이터로LDA모델.ipynb](https://github.com/jaedeokhan/ducbd-20-1-socialweb/blob/master/Crawling/0617WED_%EC%88%98%EC%A7%91%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A1%9CLDA%EB%AA%A8%EB%8D%B8.ipynb)

