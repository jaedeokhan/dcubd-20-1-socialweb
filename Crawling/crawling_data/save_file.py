def save_news_file(news_datas):
    file = open("naver_news.csv", mode="w", encoding='utf-8', newline='')
    writer = csv.writer(file)
    writer.writerow(["인덱스", "검색어", "날짜", "신문사", "제목", "내용"])
    for news in news_datas:
        writer.writerow(list(news.values()))