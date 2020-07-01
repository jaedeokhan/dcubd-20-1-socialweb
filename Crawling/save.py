import csv
from select_data import save_to_list

news_datas = save_to_list()

def save_to_csv(news_datas):
    file = open("csvname.csv", mode="w", encoding='utf-8', newline='')
    writer = csv.writer(file)
    writer.writerow(["인덱스", "검색어", "날짜", "신문사", "제목", "내용"])
    for news in news_datas:
        writer.writerow(list(news.values()))
        
save_to_csv(news_datas)