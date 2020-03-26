# SocialWebMining

## 1. 웹 마이닝이란? -> https://datamod.tistory.com/26
* 웹 마이닝은 웹자원으로부터 의미있는 패턴, 프로파일, 추세 등을 발견하기 위하여 데이터마이닝 기술을 응용한 것이다. 기존 데이터 마이닝 기술을 웹에 응용하여 웹에서 얻어지는 모든 데이터를 분석 대상으로 삼는다. 대상이 되는 데이터는 서버 접속 로그 데이터, 사용자 등록 정조, 사용자 세션, 트랜잭션, ERP(Enterprise Resource Planning) 데이터 등이 있다.

### 1.1 웹 마이닝의 분야
1. 웹 구조 마이닝
> 웹 구조 마이닝은 웹 사이트와 웹 페이지의 구조적 요약 정보를 얻는 것을 목표로 한다. 웹 사이트이 구조적 정보란, 웹 페이지 사이의 하이퍼링크를 통한 그래프 구조를 뜻한다.  -> <strong>노드, 연결구조 분석하는 기법<, 하이퍼링크로부터 패턴 찾아내거나 웹 페이지 구조 분석/strong>

2. 웹 내용 마이닝
> 웹 내용 마이닝은 실제 웹 사이트를 구성하고 있는 페이지로부터 의미 있는 내용을 추출하는 기법이다. 이는 일종의 정보의 추출이라고도 할 수 있고, 텍스트 마이닝 기술과도 밀접한 관련이 있다. 즉, 온라인에 있는 방대한 웹 데이터(텍스트, 그림, 사운드 등)에서 유용한 정보를 자동으로 찾는 기술이다.

3. 웹 사용 마이닝
> 웹 사용 마이닝은 웹 사용자의 사용 패턴을 분석하는 것이다. 이를 통해 웹 사용자의 행동을 접속 통계 정보 이상으로 이해 할 수 있고, 또한 웹 페이지의 이용 패턴을 알 수 있게 된다. 이러한 정보를 통해 사용자에게 더욱 친숙하게 페이지를 재구성하거나, 웹 서버 로드 밸런스, 사용자별 맞춤형 웹 페이지 구성 등에 이용된다.

### 1.2 데이터 수집 -> 전처리 과정 -> 웹 데이터 마이닝 분석 -> 사후 처리 
소셜 웹 마이닝은 SNS에서 사람들의 네트워크 관계와 주고받는 대화의 내용을 통해 영향력 있는 사람이 누구인지, 어떤 주제가 관심을 받는지 등을 분석한다.

### 2. 소셜 웹 마이닝 책 소개
소셜 웹 데이터를 분석하여 누가 누구와 친분관계가 있고, 무엇에 대해 대화하고, 어디에 사는지, 어떻게 찾아낼 수 있을까? 이 개정판은 더 폭넓은 내용으로 수정하였으며, 페이스북, 링크드인, 구글플러스, 깃허브, 이메일 , 웹 사이트, 블로그와 같은 모든 소셜 웹으로부터 데이터를 수집, 분석, 요약하는 방법을 제시한다.

### 2.1 목차
1. 트위터 마이닝 -> 유행하는 토픽 탐색, 사람들이 무엇에 대하여 이야기하고 있는가?
2. 페이스북 마이닝 -> 팬 페이지, 친구 관계(소셜 그래프 API 탐험)
3. 링크드인 마이닝 -> 직책 다면화, 동료들 클러스터링
4. 구글 플러스 마이닝 -> 문서 유사도 계산, 연어 추출(TF-IDF)
  * TF-IDF란? => (Term Frequency - Inverse Document Frequency) -> https://nesoy.github.io/articles/2017-11/tf-idf
  * 정보 검색과 텍스트 마이닝에서 이용하는 가중치로, 여러 문서로 이루어진 문서군이 있을 때 어떤 단어가 특정 문서내에서 얼마나 중요한 것인지를 나타내는 통계적 수치이다.
  * TF는 문서 빈도, IDF 역문서 빈도라고 한다.
  * TF-IDF는 TF와 IDF를 곱한 값으로 점수가 높은 단어일수록 다른 문서에는 많지 않고 해당 문서에서 자주 등장하는 단어를 의미한다.
 5. 웹 페이지 마이닝 -> 자연언어처리, 블로그 요약 
 6. 메일박스 마이닝 : 누가 누구에게 무엇에 대해, 얼마나 자주 이야기하는지 분석 
 7. 깃허브 마이닝 : 소프트웨어 협업 관습 살펴보기, 관심 그래프 그리기 
 8. 의미론적 마크업 웹 파이닝 : 마이크로포맷 추출, RDF 기반 추론
 9. 
 
 ### 책 pdf -> https://books.google.co.kr/books?id=EXJ9DwAAQBAJ&printsec=frontcover&hl=ko&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false
 
 ### Chapter 1. Mining Twitter : Exploring Trending Topics, Discovering What People Are People Are Talking About, and More
 * Overview
 > In this chapter, we'll ease into the process of getting situated with a minimal (but effective) development environment with Python, survey Twitter's API, and distill some analytical insights from tweets using frequency analysis. Topics that you'll learn about in this chapter include:
 * Twitter's developer platfrom and how to make API requests
 * Tweet metadata and how to use it
 * Extracting entitles such as user mentions, hashtags, and URLs from tweets
 * Techniques for performing frequency analysis with Python
 * Plotting histograms of Twitter data with the Jupyter Notebook
 
 ### Chapter 2. Mining Facebook: Analyzing Fan Pages, Examining Friendships, and More
 In this chpater, we'll tap into the Facebook platform through its (Social) Graph API and explore some of the vast possibilities.
 
 * Overview
 As this is the second chapter in the book, the concepts we'll cover are a bit more complex than those in Chapter 1, but they should still be highly accessible to a broad audience, In this chapter you'll learn about:
 * Facebook's Graph API and how to make API reqeusts
 * The Open Graph protocol and its relationship to Facebook's social graph
 * Programmatically accessing the feeds of public pages, such as those of major brands and celebrities
 * Extracting key social metrics, such as the number of likes, comments, and shares, as a measure of audience engagement
 * Manipulating data using pandas DataFrames, then visualizing the results
 
 ### Chapter 3. Mining Instagram: Computer Vision, Neural Networks, Object Recognition, and Face Detection
 In previous chapters we have focused on how to analyze text-based data retrieved from socail networks, the structure of the networks themselves, or how stronly people in your network are engaging with the contetn posted to the platform.
 
 ### 3장. 마이닝 인스 타 그램 : 컴퓨터 비전, 신경망, 물체 인식 및 얼굴 감지
 이전 장에서는 소셜 네트워크에서 검색된 텍스트 기반 데이터를 분석하는 방법, 네트워크 자체의 구조 또는 네트워크에있는 사람들이 플랫폼에 게시 된 컨텐츠에 얼마나 강한 영향을 미치는지에 중점을 두었습니다. 소셜 네트워크 인 Instagram은 주로 이미지 및 비디오 공유 앱입니다. 2010 년에 시작되어 빠르게 인기를 얻었습니다. 이 앱을 사용하면 사진을 쉽게 편집하고 다양한 필터를 적용 할 수 있습니다. 스마트 폰용으로 제작되었으므로 사진을 세상과 쉽게 공유 할 수있는 방법이되었습니다.
 
 이 장에서는 신경망의 작동 방식을 소개합니다. 손으로 쓴 숫자를 인식하기 위해 간단한 신경망을 만들 것입니다. 파이썬은 강력한 머신 러닝 라이브러리 덕분에 상당히 간단합니다. 그런 다음 Google의 Vision API를 사용하여 Instagram 피드 사진에서 물체와 얼굴을 인식하는 데 도움이됩니다. 우리는 Instagram의 API에 액세스하는 작은 테스트 응용 프로그램을 구축하기 때문에 자신의 피드에서 사진 만 사용할 수 있으므로 코드 예제를 실행하려면 Instagram 계정과 최소한 몇 장의 사진이 필요합니다 플랫폼에 게시했습니다
 
 * 개요
 이 장에서는 인공 지능에서의 적용으로 인해 최근 많은 관심을 받고있는 주제 인 기계 학습을 소개합니다. 다양한 문제에 머신 러닝을 적용하는 수천 명의 신생 기업이 등장했습니다. 이 장에서는 주로 이미지 중심의 소셜 미디어 플랫폼에서 검색된 이미지 데이터에이 기술을 적용하는 방법을 살펴 봅니다. 특히 다음에 대해 배우게됩니다.
 
 * Instagram의 API 및 API 요청 방법
 * Instagram의 API를 통해 검색된 데이터의 구조
 * 신경망의 기본 아이디어
 * 신경망을 사용하여 이미지를 "보고"그 안에있는 물체를 인식하는 방법
 * Instagram 피드에 게시물 내부의 물체와 얼굴을 인식하기 위해 강력한 사전 훈련 된 신경망을 적용하는 방법
 
 ### Instagram API 살펴보기
 Instagram API에 액세스하려면 앱을 만들고 등록해야합니다. 이것은 Instagram 개발자 플랫폼 에서 상당히 쉽게 수행 할 수 있습니다 . 여기에서 새 고객을 등록하고 이름과 설명 (예 : "my test application")을 제공 한 다음 웹 사이트 (예 : www.google.com ) 로 리디렉션 URL을 설정하십시오 . 리디렉션 URL의 이유는 곧 명확해질 것입니다.

### 4 장. LinkedIn 링크 : 직무 제목, 클러스터링 동료 및 기타 정보
이 장에서는 전문가 및 비즈니스 관계에 중점을 둔 소셜 네트워킹 사이트 인 LinkedIn에서 수집 한 데이터를 채굴하기위한 기술과 고려 사항을 소개합니다. LinkedIn은 처음에 다른 소셜 네트워크처럼 보일 수 있지만 API 데이터의 특성은 본질적으로 매우 다릅니다. 저녁 식사 대화에 적합한 것들에 대해 친구와 가족이 가득한 매우 큰 방에 트위터를 마을 광장이나 페이스 북과 같은 바쁜 공개 포럼에 비유한다면, 준공식이있는 비공개 이벤트에 링크드 인을 비유 할 수 있습니다 모든 사람이 최선의 행동을하고 전문 시장에 가져올 수있는 특정 가치와 전문 지식을 전달하려고하는 복장 규정.

LinkedIn에 집어 넣은 데이터의 다소 민감한 특성을 감안할 때 API에는 자체 뉘앙스가 있어이 책에서 보는 다른 많은 요소와 약간 다릅니다. LinkedIn에 가입 한 사람들은 기본적으로 임의의 사교와는 달리 제공되는 비즈니스 기회에 관심이 있으며 비즈니스 관계, 직업 이력 등에 대한 민감한 세부 정보를 제공 할 것입니다. 예를 들어, 일반적으로 모든 세부 사항을에 대해 접근 할 수있는 동안 당신의링크드 인 연결, 교육 이력 및 이전 작업 위치를 통해 임의의 두 사람이 "상호 적으로 연결되어 있는지"확인할 수 없습니다. 이러한 API 메소드가없는 것은 의도적 인 것입니다. API는 Facebook이나 Twitter와 같은 소셜 그래프로 모델링되지 않으므로 사용 가능한 데이터에 대해 다른 유형의 질문을해야합니다.

이 장의 나머지 부분에서는 LinkedIn API를 사용하여 데이터에 액세스하도록 설정하고 다음과 같은 종류의 질문에 대답하기 위해 유사성 측정에 따라 동료를 클러스터링하는 데 도움이되는 몇 가지 기본 데이터 마이닝 기술을 소개합니다.
* 직책과 같은 기준에 따라 가장 비슷한 연결은 무엇입니까?
* 당신이 일하고 싶은 회사에서 어떤 연결을 했습니까?
* 대부분의 연결은 지리적으로 어디에 있습니까?

모든 경우에 클러스터링 기법을 사용한 분석 패턴은 본질적으로 동일합니다. 연결 프로파일의 데이터에서 일부 기능을 추출하고, 유사성 측정을 정의하여 각 프로파일의 기능을 비교하고, 클러스터링 기법을 사용하여 “충분히 비슷합니다.” 이 접근 방식은 LinkedIn 데이터에 적합하며 동일한 기술을 다른 모든 종류의 데이터에 적용 할 수 있습니다.

### 개요
이 장에서는 머신 러닝의 기초가되는 내용을 소개하며 일반적으로 이전의 두 장보다 조금 더 고급입니다. 여기에 제시된 자료를 다루기 전에 앞의 두 장을 확실히 파악하는 것이 좋습니다. 이 장에서는 다음에 대해 배웁니다.

* LinkedIn 개발자 플랫폼 및 API 요청
* 거의 모든 문제 영역에 적용되는 기본 기계 학습 주제 인 세 가지 일반적인 유형의 클러스터링
* 데이터 정리 및 표준화
* 지오 코딩, 텍스트 참조에서 위치까지 일련의 좌표에 도달하는 수단
* Google 어스 및지도 제작을 사용하여 지리 데이터 시각화

### LinkedIn API 탐색
의미있는 방식으로이 장의 예를 따라 가려면 LinkedIn 계정과 전문가 네트워크에 대한 소수의 연결이 필요합니다. LinkedIn 계정이 없더라도 다른 도메인에 대해 배우게 될 기본 클러스터링 기술을 계속 적용 할 수 있지만이 장은 사용자가 없으면 예제를 따라갈 수 없기 때문에 매력적이지 않습니다. 자신의 링크드 인 데이터. 프로페셔널 한 삶에 가치있는 투자가 없다면 LinkedIn 네트워크를 개발하십시오.

이 장의 대부분의 분석은 다운로드 할 수있는 LinkedIn 연결의 쉼표로 구분 된 값 (CSV) 파일에 대해 수행되지만이 섹션에서는 LinkedIn API에 대한 개요를 제공하여이 책의 다른 장과 연속성을 유지합니다. LinkedIn API에 대해 배우고 싶지 않고 분석으로 바로 넘어가려면 “LinkedIn Connections를 CSV 파일로 다운로드”로 건너 뛰고 나중에 API 요청에 대한 세부 정보로 돌아가십시오.

### LinkedIn API 요청하기
Twitter 및 Facebook과 같은 다른 소셜 웹 속성 (앞 장에서 설명)과 마찬가지로 LinkedIn에 API 액세스 권한을 얻는 첫 단계는 응용 프로그램을 만드는 것입니다. 개발자 포털을 통해 샘플 애플리케이션을 작성할 수 있습니다 . 응용 프로그램의 클라이언트 ID와 클라이언트 암호를 기록하고 싶을 것입니다. 이들은 인증 자격 증명으로 API에 프로그래밍 방식으로 액세스하는 데 사용됩니다. 그림 4-1 은 응용 프로그램을 만든 후에 표시되는 양식을 보여줍니다.

와 필요한 OAuth 자격 증명이있는 경우 개인 데이터에 대한 API 액세스 권한을 얻는 프로세스에는 API 자격 증명을 만드는 데 필요한 세부 정보를 처리 할 라이브러리에 이러한 자격 증명을 제공하는 과정이 포함됩니다. 책의 가상 머신 경험을 활용하지 않는 경우,pip install python3-linkedin터미널 에 입력하여 설치해야합니다 .

## 5 장. 텍스트 파일 마이닝 : 문서 유사성 계산, 배열 추출 등
이 장에서는 텍스트 마이닝 1의 몇 가지 기본 개념을 소개 하며이 책에서는 다소 변곡점입니다. Twitter 데이터에 대한 기본 빈도 분석으로 책을 시작하고 LinkedIn 프로필에서 더 복잡한 데이터에 대한보다 복잡한 클러스터링 분석을 점차적으로 진행했지만이 장에서는 TF- IDF, 코사인 유사성 및 배열 탐지. 따라서 그 내용은 이전 장의 내용보다 약간 더 복잡하므로 여기에서 픽업하기 전에 해당 장을 살펴 보는 것이 도움이 될 수 있습니다.

가능한 한 바퀴를 재발견하지 않고 분석 도구를 처음부터 다시 작성하지는 않지만, 텍스트 마이닝을 이해하는 데 필수적인 기초적인 주제가 생길 때 몇 가지 "심해 다이빙"을 수행합니다. NLTK (Natural Language Toolkit)는 4 장 에서 기억할 수있는 강력한 기술입니다. . 이 장에서 사용할 많은 도구를 제공합니다. 풍부한 API 제품군은 처음에는 압도적이지만 걱정할 필요는 없습니다. 텍스트 분석은 엄청나게 다양하고 복잡한 연구 분야이지만, 너무 중요한 정보 없이는 먼 길을 취할 수있는 강력한 기본 사항이 많이 있습니다. 투자. 이 장과 그 이후의 장은 그러한 기본 사항을 연마하기위한 것입니다. (ㅏNLTK에 대한 완전한 소개는이 책의 범위를 벗어나지 만 NLTK 웹 사이트 에서 Python을 사용한 자연어 처리 : 자연어 툴킷을 사용한 텍스트 분석 (O'Reilly) 의 전문을 검토 할 수 있습니다 .)

### 개요
이 장에서는 블로그 게시물과 비슷한 작은 텍스트 파일 모음을 사용하여 인간 언어 데이터 분석을 시작합니다. 이 장에서는 다음에 대해 배웁니다.
* 문서의 단어를 분석하는 기본 기술인 TF-IDF (Term Frequency-Inverse Document Frequency)
* 인간 언어 이해 문제에 NLTK를 적용하는 방법
* 키워드로 문서 쿼리와 같은 일반적인 문제에 코사인 유사성을 적용하는 방법
* 배열 패턴을 감지하여 인간 언어 데이터에서 의미있는 문구를 추출하는 방법

### 텍스트 파일
오디오 및 비디오 컨텐츠는 현재 널리 보급되어 있지만 텍스트는 디지털 세계에서 계속 지배적 인 의사 소통 방식이며 상황은 조만간 변경되지 않을 것입니다. 텍스트 데이터에서 휴먼 언어에서 의미있는 통계를 컴파일하고 추출하는 데 필요한 최소한의 기술을 개발하면 소셜 웹 및 기타 직업 생활에서 경험할 수있는 다양한 문제에 대한 상당한 활용이 가능합니다. 일반적으로 소셜 웹 API를 통해 노출 된 텍스트 데이터는 본격적인 HTML이거나 <br />아포스트로피를위한 이스케이프 된 HTML 엔티티와 같은 일부 기본 마크 업이 포함되어 있다고 가정해야합니다 . 따라서 모범 사례로 정리를 위해 약간의 추가 필터링을 수행해야합니다. 예 5-1content을 도입하여 메모 필드 에서 일반 텍스트를 증류하는 방법의 예를 제공합니다 .함수가 호출되었습니다 cleanHtml.BeautifulSoupHTML 엔터티를 일반 텍스트로 다시 변환하는 HTML 조작을위한 편리한 패키지를 활용 합니다. 아직 경험하지 못한 경우 BeautifulSoup도구 상자에 도구를 추가하지 않고는 살기 원하지 않는 패키지입니다. HTML이 유효하지 않거나 표준을 위반하더라도 합리적인 방식으로 HTML을 처리 할 수 ​​있습니다. 다른 합리적인 기대치 (일명 웹 데이터).패키지를 pip install beautifulsoup4아직 설치 하지 않았다면 설치해야합니다 .


## 6 장. 마이닝 웹 페이지 : 자연어 처리 를 사용하여 인간의 언어 이해 , 블로그 게시물 요약 등
어 원천에 적용하려는 겸손한 시도입니다. 1 하고 소셜 웹 (또는 다른 곳)에서 접할 데이터에 .이전 장에서는 정보 검색 이론 (IR)에서 일부 기본 기술을 소개했는데,이 기법은 일반적으로 텍스트를 벡터로 모델링하고 조작 할 수있는 문서 중심의 "단어 모음"(정렬되지 않은 단어 모음)으로 취급합니다. 이러한 모델은 많은 상황에서 종종 잘 수행되지만 반복되는 단점은 단어를 의미하는 바로 그 문맥에서 신호를 최대화하지 않는다는 것입니다.

이 장에서는 문맥 기반의보다 다양한 기술을 사용하여 인간 언어 데이터의 의미에 대해 더 깊이 탐구합니다. 잘 정의 된 스키마에 맞는 데이터를 반환하는 소셜 웹 API는 필수이지만, 가장 기본적인 인간 커뮤니케이션 통화는이 페이지에서 읽는 단어, Facebook 게시물, 트윗에 연결된 웹 페이지 및 등등. 휴먼 언어는 지금까지 가장 보편적 인 데이터 유형이며, 데이터 중심 혁신의 미래는 디지털 형식의 인간 커뮤니케이션을 이해하기 위해 기계를 효과적으로 활용할 수있는 능력에 달려 있습니다.

### 노트
이 장을 시작하기 전에 이전 장의 내용에 대한 실무 지식이 있어야합니다. NLP를 잘 이해하면 TF-IDF, 벡터 공간 모델 등의 기본 강점과 약점에 대한 이해와 실무 지식이 전제됩니다. 이와 관련하여이 장과 그 이전 장은이 책의 다른 장들보다 다소 밀접한 결합을 갖습니다.

이전 장의 정신에서, 우리는 본질적으로 복잡한 주제에 대한 일반적인 이해를 강화하는 데 필요한 최소한의 세부 사항을 다루면서도 충분히 기술적 인 드릴 다운을 제공합니다. 일부 데이터를 즉시 채굴 할 수 있습니다. 계속해서 모퉁이를 자르고 80 %의 작업을 수행하는 데 사용할 수있는 기술의 20 %를 결정하려고 시도하는 동안 (어떤 책에서든 단일 장 또는 소규모의 여러 권의 책을 제외하고는) 이 장의 내용은 소셜 웹에서 찾을 수있는 인간 언어 데이터로 꽤 놀라운 일을 할 수있는 충분한 정보를 제공하는 실용적인 소개입니다. 웹 페이지 및 피드에서 인간 언어 데이터를 추출하는 데 중점을두고 있지만,

### 개요
이 장에서는 휴먼 언어 데이터를 분석하는 여정을 계속하고 임의의 웹 페이지와 피드를 기본으로 사용합니다. 이 장에서는 다음에 대해 배웁니다.
* 웹 페이지를 가져 와서 인간 언어 데이터 추출
* 자연어 처리의 기본 작업을 완료하기 위해 NLTK 활용
* NLP의 상황 별 분석
* NLP를 사용하여 문서 요약 생성과 같은 분석 작업 완료
* 예측 분석과 관련된 도메인의 품질 측정을위한 지표

### 웹 스크랩 핑, 파싱 및 크롤링
이 같은 프로그래밍 언어 또는 터미널 유틸리티를 사용하는 사소한 비록 curl또는 wget당신이 페이지에서 원하는 분리 된 텍스트를 추출, 임의의 웹 페이지를 가져 오지 사소한로 확실히 아니다. 텍스트는 확실히 페이지에 있지만 탐색 막대, 머리글, 바닥 글, 광고 및 기타 관심없는 노이즈 소스와 같은 다른 "보일러 플레이트"컨텐츠도 많이 있습니다. 따라서 나쁜 소식은 HTML 태그를 제거해도 상용구 자체를 제거하기 위해 아무것도 수행하지 않기 때문에 솔루션이 HTML 태그를 제거하고 남은 텍스트를 처리하는 것만 큼 간단하지 않다는 것입니다. 경우에 따라 실제로는 페이지에서 찾고자하는 신호보다 노이즈를 발생시키는 더 많은 상용구가 페이지에있을 수 있습니다.

좋은 소식은 관심있는 컨텐츠를 식별하는 데 도움이되는 도구가 수년 동안 계속 성숙해 왔으며 텍스트 마이닝 목적으로 원하는 자료를 격리 할 수있는 훌륭한 옵션이 있다는 것입니다. 또한 RSS와 같은 피드의 상대적 편재성Atom은 피드를 사용할 수있을 때 피드를 가져 오는 데 대한 예측이있을 경우 일반적으로 웹 페이지에있는 모든 문제없이 깔끔한 텍스트를 검색하는 프로세스를 지원할 수 있습니다.

웹 스크래핑 (웹 페이지에서 텍스트를 추출하는 프로세스)을 위한 훌륭한 도구 중 하나 는 웹 페이지 boilerpipe에서 상용구를 식별하고 제거하도록 설계된 Java 기반 라이브러리입니다.이 라이브러리는 "얕은 텍스트 기능을 사용한 보일러 플레이트 감지" 라는 제목의 발행 된 논문을 기반으로하며 , 감독 된 머신 러닝 기술을 사용 하여 상용구 및 페이지의 내용을 분기하는 효과를 설명합니다 .지도 학습 기법에는 해당 영역을 대표하는 훈련 샘플에서 예측 모델을 생성하는 프로세스가 포함되므로 boilerpipe정확도를 높이기 위해 조정하려는 경우 사용자 정의 할 수 있습니다.

일반적인 경우에 작동하는 기본 추출기, 기사를 포함하는 웹 페이지에 대해 훈련 된 추출기 및 페이지에서 가장 큰 텍스트 본문을 추출하도록 훈련 된 추출기가 있으며,이 경향이있는 웹 페이지에 적합 할 수 있습니다 하나의 큰 텍스트 블록이 있습니다. 어쨌든 잡음이 있거나주의가 필요할 수있는 다른 기능에 따라 텍스트에 약간의 사후 처리가 여전히 필요할 수 있지만 boilerpipe, 무거운 물건을 들어 올리는 것은 쉬운 일이 아닙니다. .

라이브러리는 Java 기반이지만 Python 3 패키지 래퍼 를 사용할 수 있을 정도로 유용하고 유명 합니다. 이 패키지의 설치는 예측 가능합니다 : use pip install boilerpipe3. 시스템에 상대적으로 최신 버전의 Java가 있다고 가정하면이 모든 것이 사용되어야합니다 boilerpipe.

예제 6-1 에서는 생성자에 ArticleExtractor전달 된 매개 변수 로 표시되는 기사의 본문 내용을 추출하는 작업에 대한 다소 간단한 사용법을 보여주는 샘플 스크립트를 보여줍니다 Extractor. 또한 시도 할 수 의 호스팅 버전boilerpipe 이와 같은로서의 제공된 다른 추출기 중 일부 차이 볼 온라인 LargestContentExtractor또는 DefaultExtractor.

## 7 장. 마이닝 사서함 : 누가 무엇을, 어떻게 자주, 누가 이야기 하는지 분석
메일 자료실은 궁극적으로 소셜 웹 데이터의 궁극적 인 종류이며 최초의 온라인 소셜 네트워크의 기초입니다. 메일 데이터는 어디에나 있으며 각 메시지는 본질적으로 사회적이며 두 명 이상의 대화와 상호 작용을 포함합니다. 또한 각 메시지는 본질적으로 표현적인 휴먼 언어 데이터로 구성되며, 특정 시간 범위와 모호하지 않은 아이덴티티에서 휴먼 언어 데이터를 고정하는 구조화 된 메타 데이터 필드와 연결됩니다. 마이닝 사서함은 확실히 이전 장에서 배운 모든 개념을 종합 할 수있는 기회를 제공하며 귀중한 통찰력을 발견 할 수있는 놀라운 기회를 제공합니다.

기업의 CIO이고 추세 및 패턴에 대한 회사 커뮤니케이션을 분석하려는 경우 통찰력을 얻기 위해 온라인 메일 링리스트를 마이닝하는 데 관심이 있거나 자신 을 정량화하는 과정에서 패턴에 대한 자신의 사서함을 탐색하고 싶을 것입니다. 다음 토론은 시작하는 데 도움이되는 입문서를 제공합니다. 이 장에서는 다음과 같은 질문에 대답하기 위해 사서함을 탐색하기위한 몇 가지 기본 도구와 기술을 소개합니다.

* 누가 누구에게 메일을 보내는가?
* 가장 많은 메일 채터가 발생하는 특정 시간 (또는 요일)이 있습니까?
* 어떤 사람들이 서로에게 가장 많은 메시지를 보내나요?
* 가장 활발한 토론 주제의 주제는 무엇입니까?

소셜 미디어 사이트는 페타 바이트에 가까운 실시간 소셜 데이터를 쌓아 올리고 있지만 소셜 네트워킹 데이터는 서비스 제공 업체가 중앙에서 관리하여 액세스하는 방법과 사용자에 대한 정확한 규칙을 작성해야한다는 중요한 결점이 여전히 남아 있습니다. 그것을 할 수 있고 할 수 없습니다. 반면에 메일 보관소는 웹에 분산되어 분산되어 있으며 다양한 주제에 대한 풍부한 메일 링리스트 토론과 사람들이 자신의 계정에 넣은 수천 개의 메시지를 표시합니다. 생각해 보면 메일 보관소를 효과적으로 채굴 할 수있는 것이 데이터 마이닝 도구 상자에서 가장 중요한 기능 중 하나 인 것처럼 보입니다.

실례로 실제 소셜 데이터 세트를 찾기가 쉽지는 않지만,이 장에서는 법률 1 이나 개인 정보 보호 문제 를 유발하지 않고 분석 기회를 극대화하기 위해 상당히 잘 연구 된 Enron 모음 을 기본으로 보여줍니다 . 데이터 세트를 잘 알려진 Unix 메일 박스 (mbox) 형식으로 표준화하여 공통 도구 세트를 사용하여 처리 할 수 ​​있습니다. 마지막으로 플랫 파일에 저장하는 JSON 형식으로 데이터를 처리하도록 선택할 수도 있지만, 2 장 에서 소개 한 강력한 데이터 분석 라이브러리를 활용 하여 강력한 인덱싱 및 쿼리를 구성 할 수 있습니다. 데이터에 대한 운영.pandas

### 개요
메일 데이터는 엄청나게 풍부하며이 책에서 지금까지 배운 모든 내용과 관련된 분석 기회를 제공합니다. 이 장에서는 다음에 대해 배웁니다.
* 메일 데이터를 편리하고 이식 가능한 형식으로 표준화하는 프로세스
* pandas, 테이블 형식 데이터에 대한 작업을 수행하기위한 Python 용 강력한 데이터 분석 라이브러리
* Enron 코퍼스 (Enron corpus) : Enron 스캔들 당시 직원 사서함의 내용으로 구성된 공개 데이터 세트
* 사용하여 pandas임의의 방법으로 엔론 코퍼스를 조회
* 분석을 위해 자신의 사서함 데이터에 액세스하고 내보내는 도구

### 메일 코퍼스 입수 및 처리
이 섹션에서는 메일 모음을 가져 와서 표준화 된 Unix mbox 형식으로 변환 한 다음 mbox를로 가져 와서 pandas DataFrame데이터를 저장하고 쿼리하기위한 범용 오브젝트 역할을합니다. 작은 가상의 사서함을 분석 한 다음 Enron 모음을 처리합니다.

## 8 장. 마이닝 GitHub : 소프트웨어 협업 습관 검사, 관심 그래프 작성 등
GitHub는 최근 몇 년 동안 믿을 수 없을 정도로 단순한 전제로 사실상 소셜 코딩 플랫폼으로 급속히 발전했습니다. 개발자가 Git 이라는 오픈 소스 분산 버전 제어 시스템 을 사용하여 오픈 소스 소프트웨어 프로젝트를 작성하고 유지 관리 할 수있는 최고의 호스팅 솔루션을 제공하십시오 . CVS 또는 Subversion 과 같은 버전 제어 시스템과 달리 Git을 사용하면 코드 기반의 정식 사본이 없습니다. 모든 복사본은 작업 복사본이며 개발자는 중앙 서버에 연결하지 않고도 작업 복사본에 대한 로컬 변경 내용을 커밋 할 수 있습니다.

분산 버전 제어 패러다임은 프로젝트에 관심이있는 개발자가 코드 저장소의 작업 복사본 을 포크 하고 개발자와 동일한 방식으로 즉시 작업을 시작할 수 있기 때문에 GitHub의 소셜 코딩 개념에 매우 적합합니다. 포크를 소유 한 사람이 작업합니다.Git은 리포지토리를 임의로 분기 할 수있는 의미를 추적 할뿐만 아니라 분기 된 하위 리포지토리 에서 변경 사항을 상위 리포지토리 로 다시 쉽게 병합 할 수 있습니다 . GitHub 사용자 인터페이스를 통해이 워크 플로우를 풀 요청 이라고합니다 .

기만적으로 단순한 개념이지만, 개발자가 최소한의 오버 헤드 (Git 작동 방식에 대한 기본 세부 사항을 이해 한 후)를 포함하는 우아한 워크 플로우를 사용하여 코딩 프로젝트를 작성하고 협업 할 수있는 능력은 혁신을 방해하는 많은 지루한 세부 사항을 확실히 간소화했습니다 데이터 시각화 및 다른 시스템과의 상호 운용성을 초월하는 편의성을 포함한 오픈 소스 개발 즉, GitHub를 오픈 소스 소프트웨어 개발의 인 에이 블러라고 생각하십시오. 같은 방식으로 개발자들이 수십 년 동안 코딩 프로젝트에 협력 해 왔지만, GitHub와 같은 호스팅 플랫폼은 협업을 강화하고 프로젝트를 쉽게 생성하고 소스 코드를 공유하며 피드백 및 문제 추적기를 유지함으로써 전례없는 방식으로 혁신을 가능하게합니다. 개선 및 버그 수정 등을위한 패치를 수락합니다. 더 최근에는 GitHub가비 개발자에게 점점 더 많은 서비스를 제공하고 주류 협업을위한 가장 인기있는 소셜 플랫폼 중 하나가되었습니다.

완벽하게 명확하게하기 위해이 장에서는 Git 또는 GitHub를 분산 버전 제어 시스템으로 사용하는 방법에 대한 자습서를 제공하거나 어떤 수준에서든 Git 소프트웨어 아키텍처에 대해 설명하지 않습니다. (많은 훌륭한 온라인 중 하나를 참조하십시오그러나 Gitcm.com 과 같은 Git 참조는 그러한 종류의 교육을 제공합니다.) 그러나이 장에서는 다소 틈새 소프트웨어 개발 공간에서 사회적 협업 패턴을 발견하기 위해 GitHub의 API를 마이닝하는 방법을 설명하려고합니다.

### 개요
이 장에서는 소셜 코딩 플랫폼으로서 GitHub를 소개하고 NetworkX를 사용한 그래프 중심 분석에 대해 설명합니다. 이 장에서는 다양한 방법으로 사용할 수있는 데이터의 그래픽 모델을 구성하여 GitHub의 풍부한 데이터를 활용하는 방법을 배웁니다.특히, GitHub 사용자, 리포지토리 및 프로그래밍 언어 간의 관계를 관심 그래프로 취급합니다 . 이는 그래프 의 노드와 링크를 주로 사람의 유리한 지점과 해당 대상에서 해석하는 방법입니다. 관심이 있습니다. 요즘 해커, 기업가, 웹 메이븐들 사이에서 웹의 미래가 관심 그래프의 개념에 크게 좌우되는지 여부에 대해 많은 논의가 이루어 졌으므로 이제는 속도를 낼 수있는 좋은시기입니다. 떠오르는 그래프 풍경과 그에 수반되는 모든 것.

요약하면이 장은 이전 장과 동일한 예측 가능한 템플릿을 따르며 다음과 같은 내용을 다룹니다.

* GitHub의 개발자 플랫폼 및 API 요청 방법
* NetworkX를 사용하여 그래프 스키마 및 특성 그래프를 모델링하는 방법
* 관심 그래프의 개념과 GitHub 데이터에서 관심 그래프를 구성하는 방법
* NetworkX를 사용하여 특성 그래프 조회
* 정도, 중간 정도 및 근접성 중심성을 포함한 그래프 중심성 알고리즘

### GitHub의 API 탐색
처럼 이 책에 소개 된 다른 소셜 웹 속성 인 GitHub의 개발자 사이트 는 API, API 사용에 적용되는 서비스 약관, 예제 코드 등을 포괄적으로 설명합니다. API는 상당히 풍부하지만 소프트웨어 개발자, 프로젝트, 프로그래밍 언어 및 기타 소프트웨어 개발 측면을 연결하는 관심 그래프를 생성하기 위해 데이터를 수집하는 데 필요한 몇 가지 API 호출에만 중점을 둘 것입니다. API는 github.com이 제공하는 것과 같이 풍부한 사용자 경험을 구축하는 데 필요한 모든 것을 제공하며, 이러한 API로 구축 할 수있는 강력하고 유리한 응용 프로그램이 부족하지 않습니다.

GitHub의 가장 기본적인 기본 요소는 사용자 와 프로젝트 입니다. 이 페이지를 읽고 있다면 이미 GitHub 프로젝트 페이지 에서이 책의 ​​소스 코드를 풀었 을 것입니다. 따라서이 토론에서는 최소한 GitHub 프로젝트 페이지를 몇 번 방문했고 약간 찔렀다 고 가정합니다. GitHub이 제공하는 일반적인 개념에 익숙합니다.

GitHub 사용자는 일반적으로 다른 GitHub 사용자가 만들거나 분기 한 하나 이상의 코드 리포지토리를 포함하는 공개 프로필을 가지고 있습니다. 예를 들어, GitHub 사용자 ptwobrussell는 하나의 호출 된 Mining-the-Social-Web것과 다른 하나의 호출 된 것을 포함하여 두 개의 GitHub 저장소를 소유합니다 Mining-the-Social-Web-2nd-Edition. ptwobrussell또한 개발 목적으로 특정 코드 기반의 특정 작업 스냅 샷을 캡처하기 위해 여러 리포지토리를 분기했으며 이러한 분기 된 프로젝트도 그의 공개 프로필에 나타납니다.

GitHub를 강력하게 만드는 요소 중 하나는 다른 사용자와 마찬가지로 ptwobrussell이 포크 프로젝트 중 어떤 것이 든 원하는대로 할 수 있습니다 (소프트웨어 라이센스 조건에 따라). 사용자가 코드 리포지토리를 포크하면 해당 리포지토리의 작업 복사본을 효과적으로 소유하고 그 주변에서 바이올린을 사용하여 원래 프로젝트의 오래 지속되는 포크를 만들 수 있습니다. 원래 상위 저장소로 다시 병합되었습니다. 대부분의 프로젝트 포크는 자체 파생 작업으로 구체화되지는 않지만 파생 작업 생성과 관련된 노력은 소스 코드 관리 측면에서 사소한 것입니다. 수명이 짧고 상위 요청으로 다시 풀 요청으로 표시되거나 오래 지속되어 자체 커뮤니티와 완전히 별개의 프로젝트가 될 수 있습니다.

GitHub에서 프로젝트를 포크하는 것 외에도, 사용자는 프로젝트를 북마크하거나 별표를 표시 하여 프로젝트의 스타 게이 자로 알려져 있습니다. 프로젝트를 북마크하는 것은 본질적으로 웹 페이지 나 트윗을 북마크하는 것과 같습니다. 프로젝트에 관심이 있다는 것을 의미하며 빠른 참조를 위해 GitHub 책갈피 목록에 표시됩니다. 일반적으로 알 수있는 것은 북마크하는 것보다 훨씬 적은 사람들이 코드를 포크한다는 것입니다. 북 마킹은 10 년이 넘는 웹 서핑에서 쉽고 이해하기 쉬운 개념이지만 코드를 포크하는 것은 어떤 식 으로든 그것을 수정하거나 기여하려는 의도를 의미합니다. 이 장의 나머지 부분에서는 프로젝트에 대한 별표 목록을 관심 그래프 구성의 기초로 사용하는 데 중점을 둘 것입니다

### GitHub API 연결 생성
다른 소셜 웹 속성과 마찬가지로 GitHub는 OAuth 및 API 액세스 권한을 얻는 단계에는 계정을 만든 후 API 소비자로 사용할 응용 프로그램을 만들거나 계정에 직접 연결되는 "개인"액세스 토큰을 만드는 두 가지 가능성 중 하나가 포함됩니다. 이 장에서는 그림 8-1 과 같이 계정 응용 프로그램 메뉴 의 개인 액세스 API 토큰 섹션에서 버튼을 클릭하는 것만 큼 쉬운 개인 액세스 토큰을 사용하도록 선택합니다 . OAuth에 대한보다 광범위한 개요는 부록 B 를 참조하십시오 .

#### 예 8-1. GitHub의 API에 액세스하기 위해 프로그래밍 방식으로 개인 API 액세스 토큰 얻기
```python
import requests
import json

username = '' # Your GitHub username
password = '' # Your GitHub password

# Note that credentials will be transmitted over a secure SSL connection
url = 'https://api.github.com/authorizations'
note = 'Mining the Social Web - Mining Github'
post_data = {'scopes':['repo'],'note': note }

response = requests.post(
    url,
    auth = (username, password),
    data = json.dumps(post_data),
    )

print("API response:", response.text)
print()
print("Your OAuth token is", response.json()['token'])

# Go to https://github.com/settings/tokens to revoke this token
```

다른 많은 소셜 웹 속성과 마찬가지로 GitHub의 API는 HTTP를 기반으로 구축되며 터미널의 명령 줄 도구를 포함하여 HTTP 요청을 할 수있는 모든 프로그래밍 언어를 통해 액세스 할 수 있습니다. 그러나 이전 장에서 설정 한 선례에 따라 Python 라이브러리를 사용하여 요청, 응답 구문 분석 및 페이지 매김 처리와 관련된 지루한 세부 사항을 피할 수 있습니다.이 특별한 경우에는를 사용 PyGithub하여 설치할 수 있습니다.다소 예측 가능하다 pip install PyGithub. 그래픽 모델에 대한 토론으로 전환하기 전에 GitHub API 요청을 만드는 방법에 대한 몇 가지 예를 살펴 보겠습니다

이 장에서 Mining-the-Social-Web GitHub 리포지토리 에서 관심 그래프를 시드 하고 해당 스타 게이저 사이에 연결을 만들어 보겠습니다.List Stargazers API 를 사용하여 저장소의 스타 게이저를 나열 할 수 있습니다 . 웹 브라우저에서 다음 URL을 복사하여 붙여 넣어 응답 유형의 모양에 대한 아이디어를 얻기 위해 API 요청을 시도 할 수 있습니다. https://api.github.com/repos/ptwobrussell/Mining-the-Social- 웹 / 스타 게이저

#### 노트
Mining the Social Web , 3rd Edition을 읽고 있지만 ,이 장의 예제에서는 1,000 회 이상 별표가 표시된이 장의 예제에서 첫 번째 버전의 코드 저장소를 계속 사용합니다. 이 책의 두 번째 또는 세 번째 개정판의 저장소를 포함하여 저장소를 분석하는 것은 예제 8-3 에서 소개 된대로 초기 프로젝트의 이름을 변경하여 달성하기에 충분히 쉽습니다 .

이 방법으로 인증되지 않은 요청을 발행하는 기능은 API를 탐색 할 때 매우 편리하며 시간당 60 개의 인증되지 않은 요청의 제한 속도는 땜질 및 탐색에 적합합니다. 당신은, 그러나, 형태의 쿼리 문자열 APPEND 수 ?access_token=xxx, xxx액세스 토큰을 지정, 인증 된 방식으로 같은 요청을합니다. GitHub의 인증 된 속도 제한은 개발자 문서에서 속도 제한에 설명 된대로 시간당 관대 한 5,000 개의 요청입니다 . 예 8-2 는 샘플 요청 및 응답을 보여줍니다. (이 페이지는 첫 페이지의 결과 만 요청 하고 페이지 매김 에 대한 개발자 설명서에 설명 된대로결과 페이지를 탐색하기위한 메타 데이터 정보가 HTTP 헤더에 포함됩니다.)

##### 예 8-2. GitHub의 API에 대한 직접 HTTP 요청
```python
import json
import requests

# An unauthenticated request that doesn't contain an ?access_token=xxx query string
url = "https://api.github.com/repos/ptwobrussell/Mining-the-Social-Web/stargazers"
response = requests.get(url)

# Display one stargazer
print(json.dumps(response.json()[0], indent=1))
print()

# Display headers
for (k,v) in response.headers.items():
    print(k, "=>", v)
```

샘플 출력은 다음과 같습니다.
```
{
 "로그인": "rdempsey",
 "id": 224,
 "avatar_url": "https://avatars2.githubusercontent.com/u/224?v=4",
 "gravatar_id": "",
 "url": "https://api.github.com/users/rdempsey",
 "html_url": "https://github.com/rdempsey",
 "followers_url": "https://api.github.com/users/rdempsey/followers",
 "following_url": "https://api.github.com/users/rdempsey/following{/other_user}",
 "gists_url": "https://api.github.com/users/rdempsey/gists{/gist_id}",
 "starred_url": "https://api.github.com/users/rdempsey/starred{/owner}{/repo}",
 "subscriptions_url": "https://api.github.com/users/rdempsey/subscriptions",
 "organizations_url": "https://api.github.com/users/rdempsey/orgs",
 "repos_url": "https://api.github.com/users/rdempsey/repos",
 "events_url": "https://api.github.com/users/rdempsey/events{/privacy}",
 "received_events_url": "https://api.github.com/users/rdempsey/received_events",
 "type": "사용자",
 "site_admin": 거짓
}

서버 => GitHub.com
날짜 => Fri, 06 Apr 2018 18:41:57 GMT
Content-Type => application / json; 문자 집합 = UTF-8
전송 인코딩 => 청크
상태 => 200 OK
X-RateLimit-Limit => 60
X-RateLimit- 잔여 => 55
X-RateLimit-Reset => 1523042441
캐시 제어 => 공개, 최대 연령 = 60, s-maxage = 60
다름 => 수락
ETag => W / "b43b2c639758a6849c9f3f5873209038"
X-GitHub-Media-Type => github.v3; format = json
링크 => <https://api.github.com/repositories/1040700/stargazers?page=2>;
rel = "next", <https://api.github.com/repositories/1040700/stargazers?page=39>;
rel = "last"
액세스 제어 노출 헤더 => ETag, 링크, 재시도 후, X-GitHub-OTP,
X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset,
X-OAuth 범위, X- 수락 OAuth 범위, X- 폴 간격
액세스 제어 허용 출처 => *
엄격한 운송 보안 => 최대 연령 = 31536000; includeSubdomains; 예압
X- 프레임 옵션 => 거부
X- 컨텐트 유형 옵션 => nosniff
X-XSS- 보호 => 1; mode = 차단
Referrer-Policy => 출처-원산지 시점, 엄격한 출처-원산지 출처
Content-Security-Policy => default-src '없음'
X- 런타임 랙 => 0.057438
콘텐츠 인코딩 => gzip
X-GitHub-Request-Id => ADE2 : 10F6 : 8EC26 : 1417ED : 5AC7BF75
```

보시다시피, GitHub가 HTTP 응답의 본문에 있지 않고 개발자 문서에 요약 된 것처럼 HTTP 헤더로 전달되는 유용한 정보가 많이 있습니다. 다양한 헤더가 무엇을 의미하는지 이해하고 이해해야하지만, 몇 가지 참고 사항에는 status헤더가 포함되어 있는데, 이는 200 개의 응답으로 요청이 정상임을 나타냅니다. 속도 제한과 관련된 헤더 (예 : x-ratelimit-remaining; 및 link다음과 같은 값을 포함 헤더 :

```
https://api.github.com/repositories/1040700/stargazers?page=2 ; rel = "next",
 https://api.github.com/repositories/1040700/stargazers?page=29 ; rel = "last"
```

이를 통해 다음 결과 페이지를 가져 오는 데 사용할 수있는 사전 구성된 URL과 총 결과 페이지 수를 표시 할 수 있습니다.

#### GitHub API 요청하기
이기는 하지만 라이브러리를 사용하는 것이 어렵지 않고 직접 requests정보를 파싱 하여이 정보를 최대한 활용하는 것이 어렵지 않습니다. 라이브러리와 같은 라이브러리 PyGithub는 훨씬 더 쉽고 GitHub API의 구현 세부 사항 추상화를 처리하여 깨끗한 Pythonic API로 작업 할 수있게합니다. . 더 나은 방법은, GitHub가 API의 기본 구현을 변경하더라도 여전히 사용할 수 있으며 PyGithub코드가 깨지지 않습니다.

로 요청하기 전에 PyGithub응답 본문을 살펴보십시오. 여기에는 풍부한 정보가 포함되어 있지만 가장 관심있는 부분은이라는 필드입니다.이 필드 login는 사용자의 GitHub 사용자 이름입니다.관심있는 저장소에서 응시. 이 정보는 사용자가 별표 표시 한 모든 리포지토리의 목록을 반환하는 API 인 "별표가 표시되는 리포지토리" 와 같은 다른 많은 쿼리를 다른 GitHub API에 발급하는 기초입니다 . 임의 저장소로 시작하여 관심있는 사용자 목록에 대해 쿼리 한 후 해당 사용자에게 추가 관심있는 저장소를 쿼리하고 잠재적으로 발생할 수있는 패턴을 발견 할 수 있기 때문에 이는 강력한 피봇입니다.

예를 들어, Mining-the-Social-Web을 즐겨 찾기에 추가 한 모든 사용자들 중에서 가장 북마크 된 저장소가 무엇인지 아는 것이 흥미롭지 않습니까? 이 질문에 대한 대답은 GitHub 사용자가 높이 평가할 수있는 지능형 권장 사항의 기초가 될 수 있으며, 지능형 권장 사항이 응용 프로그램에서 향상된 사용자 경험을 제공 할 수있는 여러 영역을 상상하는 데 많은 창의력을 발휘하지 못합니다. 아마존과 넷플릭스의 경우. 기본적으로 관심사 그래프는 본질적으로 그러한 지능적인 추천을하는 데 적합하며, 늦게 특정 틈새 시장에서 관심사 그래프가 이러한 대화 주제가 된 이유 중 하나입니다.

예 8-3 에서는 PyGithub리포지토리에 대한 모든 스타 게이저를 검색하여 관심 그래프를 시드하는 데 사용할 수있는 방법의 예를 제공합니다 .

##### 예 8-3. PyGithub를 사용하여 특정 저장소의 스타 게이저 쿼리
```python
from github import Github # pip install pygithub

# Specify your own access token here

ACCESS_TOKEN = ''

# Specify a username and a repository of interest for that user

USER = 'ptwobrussell'
REPO = 'Mining-the-Social-Web'
#REPO = 'Mining-the-Social-Web-2nd-Edition'

client = Github(ACCESS_TOKEN, per_page=100)
user = client.get_user(USER)
repo = user.get_repo(REPO)

# Get a list of people who have bookmarked the repo.
# Since you'll get a lazy iterator back, you have to traverse
# it if you want to get the total number of stargazers.

stargazers = [ s for s in repo.get_stargazers() ]
print("Number of stargazers", len(stargazers))
```

배후에서 PyGithubAPI 구현 세부 사항을 처리하고 쿼리를위한 편리한 객체를 노출합니다. 이 경우 GitHub에 대한 연결을 만들고per_page키워드 매개 변수는 각 데이터 페이지의 기본 숫자 (30)와 반대로 최대 결과 수 (100)를 받고 싶다고 알려줍니다. 그런 다음 특정 사용자를위한 리포지토리를 가져오고 해당 리포지토리의 별표를 쿼리합니다. 사용자가 동일한 이름의 리포지토리를 가질 수 있으므로 리포지토리 이름만으로 명확하게 쿼리 할 수있는 방법은 없습니다. 사용자 이름과 저장소 이름이 겹칠 수 있으므로 이러한 이름 중 하나를 식별자로 사용하는 경우 GitHub의 API를 사용할 때 작업하는 객체의 종류를 지정해야합니다. 리포지토리 나 사용자 자격을 갖추지 않으면 모호 할 수있는 노드 이름으로 그래프를 만들 때이 점을 고려해야합니다.

마지막으로 PyGithub일반적으로 결과로 "지연 반복자"를 제공합니다.이 경우 쿼리가 실행될 때 29 페이지의 결과를 모두 가져 오지 않습니다. 대신, 페이지를 검색하기 전에 데이터를 반복 할 때 특정 페이지가 요청 될 때까지 대기합니다. 이러한 이유로 정확한 카운트를 얻으려면 API로 stargazer의 수를 실제로 계산하기 위해 목록 이해를 통해 lazy iterator를 소진해야합니다.

PyGithub의 문서 는 도움이되며, API는 일반적으로 예측 가능한 방식으로 GitHub API를 모방합니다.일반적으로 파이썬 인터프리터에서 및 함수 pydoc를 통해와 같이 를 사용할 수 있습니다 . 또는 IPython 또는 Jupyter Notebook의 탭 완성 및 "물음표 마술"을 통해 어떤 객체를 호출 할 수있는 방법을 알아낼 수 있습니다. 계속 진행하기 전에 GitHub API에서 약간 의 가능성을 숙지하는 것이 좋습니다. 기술을 테스트하기위한 연습으로 Mining-the-Social-Web의 stargazer (또는 일부 하위 집합)를 반복하고 어떤 다른 리포지토리가 공통적으로 관심을 가질 수 있는지 결정하는 기본 빈도 분석을 수행 할 수 있습니까?dirhelpPyGithub주파수 통계를 쉽게 계산하는 데 파이썬 collections.Counter이나 NLTK가 nltk.FreqDist필수적이라는 것을 알게 될 것입니다..

### 속성 그래프를 사용한 데이터 모델링
2 장 에서 기억할 수 있습니다이 그래프는 Facebook의 소셜 네트워크 데이터를 표현, 분석 및 시각화하는 수단으로 전달되었습니다. 이 섹션은보다 철저한 토론을 제공하며 그래프 계산에 유용한 입문서가되기를 바랍니다. 여전히 레이더 아래에 있지만 그래프는 실제 세계에서 많은 현상을 모델링하기위한 매우 자연스러운 추상화이므로 그래프 컴퓨팅 환경이 빠르게 떠오르고 있습니다. 그래프는 데이터 표현의 유연성을 제공하여 관계형 데이터베이스와 같은 다른 옵션과 비교할 때 특히 데이터 실험 및 분석 중에 이길 수 없습니다. 그래프 중심 분석은 모든 문제에 대한 만병 통치약은 아니지만 그래픽 구조를 사용하여 데이터를 모델링하는 방법에 대한 이해는 툴킷에 강력한 추가 기능입니다.

#### 노트 
그래프 이론에 대한 일반적인 소개는이 장의 범위를 벗어납니다. 다음에 나오는 논의는 주요 개념이 발생할 때 부드럽게 소개하려고합니다. 짧은 YouTube 비디오 “그래프 이론 — 소개”를 즐길 수 있습니다 . 진행하기 전에 일반적인 배경 지식을 축적하고 싶다면

이 섹션의 나머지 부분 에서는 NetworkX 라는 Python 패키지를 통해 GitHub 데이터를 관심 그래프로 모델링하기위한 속성 그래프라는 일반적인 종류의 그래프를 소개합니다 . 속성 그래프는 노드 가있는 엔터티와 가장자리 가있는 엔터티 간의 관계 를 나타내는 데이터 구조입니다 . 각 정점에는 고유 식별자, 키 / 값 쌍으로 정의 된 속성 맵 및 모서리 모음이 있습니다. 마찬가지로 에지는 노드를 연결하고 고유하게 식별 할 수 있으며 속성을 포함 할 수 있다는 점에서 고유합니다.

도 8-2 도시 의적으로 식별되는 두 개의 노드 특성 그래프의 사소한 예 X및 Y그들 간의 관계 undescribed. 이 특정 그래프는 에지가 지향되기 때문에 디 그래프 ( digraph )라고하며 , 에지의 방향성이 모델링되는 도메인에 대한 의미에 뿌리를두고 있지 않는 한 반드시 그럴 필요는 없다.


그림 8-2. 방향이 지정된 사소한 속성 그래프
NetworkX를 사용하여 코드로 표현하면 예 8-4 와 같이 간단한 속성 그래프를 작성할 수 있습니다 . ( pip install networkx책의 턴키 가상 머신을 사용하지 않는 경우이 패키지를 설치할 수 있습니다 .)

##### 예 8-4. 사소한 속성 그래프 구성
```python
import networkx as nx # pip install networkx

# Create a directed graph

g = nx.DiGraph()

# Add an edge to the directed graph from X to Y

g.add_edge('X', 'Y')

# Print some statistics about the graph

print(nx.info(g))

# Get the nodes and edges from the graph

print("Nodes:", g.nodes())
print("Edges:", g.edges())
print()

# Get node properties

print("X props:", g.node['X'])
print("Y props:", g.node['Y'])
print()

# Get edge properties

print("X=>Y props:", g['X']['Y'])
print()

# Update a node property

g.node['X'].update({'prop1' : 'value1'})
print("X props:", g.node['X'])
print()

# Update an edge property

g['X']['Y'].update({'label' : 'label1'})
print("X=>Y props:", g['X']['Y'])
```












 
  
  
  
  
  
  
  




