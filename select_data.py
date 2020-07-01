import pymysql
import pandas as pd

def save_to_list():
    
    db = pymysql.connect(host='your ip address',
                         port=3306,
                         user='your usernmae',
                         passwd='your passwd',
                         db='your database',
                         charset='utf8')
    cursor = db.cursor()
    
    columns = ['인덱스', '검색어', '날짜', '신문사', '제목', '내용']

    df = dict()
    df_list = list()

    sql = """
        SELECT * FROM new_stock
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