import requests
from bs4 import BeautifulSoup
import json
import re
import sys
import time, random
import pandas as pd
import pymysql
from crawling import get_news

# 접속
db = pymysql.connect(host='your ip address',
                     port=3306,
                     user='your username',
                     passwd='your passwd',
                     db='your database',
                     charset='utf8')

# 커서 가져오기
cursor = db.cursor()

querys = ['코로나', '마스크', '여행']
s_date = "2020.05.22"
e_date = "2020.05.22"
s_from = s_date.replace(".", "")
e_to = e_date.replace(".", "")
page = 1

# for 문에서 querys 의 데이터를 query 로 던져주면,
# 각각의 코로나, 마스크 , 여행 하나의 for문이 끝나면 page_set 으로 다시 1로 설정
page_set = 1

# query 를 3개 던져줘서 코로나, 마스크, 여행에 대해 크롤링한다.
for query in querys:
    page = page_set  
    print (query + "start!!\n\n\n")
    while True:
        time.sleep(random.sample(range(3), 1)[0])
        print(page)
        url = "https://search.naver.com/search.naver?where=news&query=" + query +             "&sort=1&field=1&ds=" + s_date + "&de=" + e_date + \
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
                    # 제목, 날짜, 신문사, 내용 가져오는 get_news() 함수 사용
                    news_detail = get_news(urls.attrs["href"])

                    sql = """
                          INSERT INTO `naver_news` (`query`, `date`, `company`, `title`, `content`) VALUES(%s, %s, %s, %s, %s);
                          """
                    # query, date, company, title, content 
                    cursor.execute(sql, (query ,news_detail[1], news_detail[3], news_detail[0], news_detail[2]))

                    db.commit()
            except Exception as e:
                print(e)
                continue
        page += 10

    #   각각 4번 돌리고 일단 stop
        if page == 51:
            break

db.close()