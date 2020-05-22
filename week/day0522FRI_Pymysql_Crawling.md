### 2020 0522 FRI 
### Today
1. Jupyter Noteboo 에서 Pymysql 모듈을 이용해서 DB 스키마 생성
2. 네이버 뉴스 기사를 get_news(n_url): 함수로 데이터를 가져온다.
3. query는 기존에 코로나 하나를 사용했지만, 이번에는 query=['코로나', '마스크', '여행'] 과 같이 3개의 값을 for 문을 돌려서 안에 while True 문을 돌렸다.
4. <b>save_to_data()</b> : Pymysql를 통해서 저장한 DB에 select SQL을 사용해서 dict, list를 활용해서 저장하기.
5. <b>save_to_file(news_datas)</b>: df_list를 인자로 받아서 csv를 생성하는 함수
6. 전처리는 아직 하지 않고, 일단 클러스터링을 진행을 한다.
7. 클러스터링 진행

[1-6 항목 file](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0508Fri_naver_news_crawling)


#### 1. Jupyter Notebook 에서 Pymysql 모듈을 사용해서 네이버 뉴스 기사 크롤링하기
* 기존의 query = '코로나' 한 개에서 querys = ['코로나', '마스크', '여행'] 세 개의 query 로 while True 문을 돌려서 데이터를 가져오기.

<b>page를 51번으로 설정을 해서 , 각각의 쿼리 3가지를 총 4번을 돌린다. </b>

```python
import requests
from bs4 import BeautifulSoup
import json
import re
import sys
import time, random
import pandas as pd
import pymysql

# 접속
db = pymysql.connect("localhost",
                     "root",
                     "root",
                     "news")

# 커서 가져오기
cursor = db.cursor()

def get_news(n_url):
    news_detail = []
    print(n_url)
    breq = requests.get(n_url)
    bsoup = BeautifulSoup(breq.content, 'html.parser')

    # 제목 파싱
    title = bsoup.select('h3#articleTitle')[0].text
    news_detail.append(title)

    # 날짜
    pdate = bsoup.select('.t11')[0].get_text()[:10]
    news_detail.append(pdate)

    # news text
    _text = bsoup.select('#articleBodyContents')[
        0].get_text().replace('\n', " ")
    btext = _text.replace(
        "// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")
    news_detail.append(btext.strip())

    # 신문사
    pcompany = bsoup.select('#footer address')[0].a.get_text()
    news_detail.append(pcompany)

    return news_detail

columns = ['날짜', '신문사', '제목', '내용']
df = pd.DataFrame(columns=columns)

# query = '코로나'   # url 인코딩 에러는 encoding parse.quote(query)
querys = ['코로나', '마스크', '여행']
s_date = "2020.05.22"
e_date = "2020.05.22"
s_from = s_date.replace(".", "")
e_to = e_date.replace(".", "")
page = 1
page_set = 1

# while True:
#     time.sleep(random.sample(range(3), 1)[0])
#     print(page)
for query in querys:
    page = page_set  
    print (query + "start!!\n\n\n")
    while True:
        time.sleep(random.sample(range(3), 1)[0])
        print(page)
        url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=1&field=1&ds=" + s_date + "&de=" + e_date + \
            "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + \
            e_to + "%2Ca%3A&start=" + str(page)

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

        req = requests.get(url, headers=header)
        print(url)
        cont = req.content
        soup = BeautifulSoup(cont, 'html.parser')

        if soup.findAll("a", {"class": "_sp_each_url"}) == []:
            break

        for urls in soup.findAll("a", {"class": "_sp_each_url"}):
            try:
                if urls.attrs["href"].startswith("https://news.naver.com"):
                    print(urls.attrs["href"])
                    news_detail = get_news(urls.attrs["href"])
    #      abs
                    sql = """
                        INSERT INTO `new` (`query`, `date`, `company`, `title`, `content`) VALUES(%s, %s, %s, %s, %s);
                    """
#                     print(query, news_detail[1], news_detail[3], news_detail[0], news_detail[2], end=' ')
    #                 print(sql)
                    # 날짜, 신문사, 제목, 내용
                    cursor.execute(sql, (query ,news_detail[1], news_detail[3], news_detail[0], news_detail[2]))

                    db.commit()
            except Exception as e:
                print(e)
                continue
        page += 10

    #     20번 돌리고 일단 stop
        if page == 51:
            break
    
db.close()
```

#### 2. save_to_data() 함수로 정의, pymysql data inser 한 것을 select 해서 dict에 데이터를 모두 담아서 list에 각각 저장하기.

```python
def save_to_data():
    import pymysql
    import pandas as pd

    columns = ['인덱스', '검색어', '날짜', '신문사', '제목', '내용']

    df = dict()
    df_list = list()

    db = pymysql.connect("localhost",
                         "root",
                         "root",
                         "news")

    cursor = db.cursor()

    sql = """
        SELECT * FROM new
    """

    cursor.execute(sql)
    results = cursor.fetchall()

    for index, result in enumerate(results):

        index = result[0]
        query = result[1]
        date = result[2]
        company = result[3]
        title = result[4]
        content = result[5]

        df = {
            '인덱스' : index,
            '검색어' : query,
            '날짜' : date,
            '신문사' : company,
            '제목' : title,
            '내용' : content}

        df_list.append(df)

    db.commit()

    db.close()
    return df_list
```

#### 3. save_to_file(news_datas) : 위의 df_list를 news_datas의 인자로 받아서 .csv 파일을 만드는 함수

```python
import csv

news_datas = save_to_data()

def save_to_file(news_datas):
    file = open("naver_news.csv", mode="w", encoding='utf-8', newline='')
    writer = csv.writer(file)
    writer.writerow(["인덱스", "검색어", "날짜", "신문사", "제목", "내용"])
    for news in news_datas:
        writer.writerow(list(news.values()))
        
save_to_file(news_datas)
```

#### 4. K-평균 군집 분석
[7- 클러스터링 file](https://github.com/jaedeokhan/SocialWebMining/blob/master/Crawling/0521fri_news_clustering)

