import pymysql

# pymysql.connect로 MYSQL 연결 객체를 db에 전달
db = pymysql.connect(host='your ip address',
                     port=3306,
                     user='your usernmae',
                     passwd='your passwd',
                     db='your database',
                     charset='utf8')

cursor = db.cursor()

sql = """
    CREATE TABLE naver_news (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        query VARCHAR(10) NOT NULL,
        date VARCHAR(25) NOT NULL,
        company VARCHAR(15) NOT NULL,
        title VARCHAR(100) NOT NULL,
        content VARCHAR(10000) NOT NULL,
        PRIMARY KEY(id))
"""

cursor.execute(sql)
cursor.execute('desc naver_stock')
results = cursor.fetchall()

for result in results:
    print (result)

# db에 complete 하기.
db.commit()

# db 연결 닫기
db.close()