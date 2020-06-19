### 2020 0503 SUN CREATE
### 2020 0619 FRI UPDATE

### Pymysql 사용법
1. pymysql 라이브러리 소개 및 설치
   1. pymysql connector
   2. pymysql 실습 코드
   3. startwidth() fucnction 

#### 1. pymysql 라이브러리 소개 및 설치
```bash
$ pip install pymysql[rsa]
```

#### 1.1 pymysql이란?
* mysql을 python에서 사용할 수 있는 라이브러리(pymysql 라이브러리 이외에도 MySQLdb(Mysql-python), MySQL connector 등 다양한 라이브러리 존재
* 이 중에서 설치가 가장 쉬운 라이브러리
* 일반적인 mysql 핸들링 코드 작성 순서
   1. PyMySql 모듈 import
   2. pymysql.connect() 메소드를 사용하여 MySQL에 연결
      * 호스텨명, 포트, 로그인, 암호, 접속할 DB 등을 파라미터로 지정
   3. MySQL 접속이 성공하면 , Connection 객체로부터 cursor()메서드를 호출하여 Cursor 객체를 가져온다.
   4. Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 전송
   5. SQL 쿼리의 경우 Cursor 객체의 fetchall(), fetchone(), fetchmany() 등의 메서드를 이용하여 서버로부터 가져온 데이터를 코드에서 활용
   6. 삽입, 갱신, 삭제 등의 DML(Data Manipulation Languages) 문장을 실행하는 경우, INSERT/UPDATE/DELETE 후 Connection 객체의 commit() 메서드를 사용하여 데이터를 확정1
   7. Connection 객체의 close() 메서드를 사용하여 DB 연결을 닫음

#### 1.2 pymysql.connect() 메소드를 사용하여 MYSQL에 연결
* 호스트명, 포트, 로그인, 암호, 접속할 DB 등을 파라미터로 지정
* 주요 파라미터
   * host : 접속할 mysql server 주소
   * post : 접속할 mysql server의 포트 번호
   * user : mysql ID
   * passwd : mysql ID의 암호
   * db : 접속할 데이터베이스
   * charset='utf8' : mysql에서 select하여 데이터를 가져올 때 한글이 깨질 수 있으므로 연결 설정에 넣어준다.

#### 1.3 pymysql 실습 코드
```python
# 1. db에 connect하기
db = pymysql.connect(host='ip주소',
                     port=3306,
		     user='유저이름',
		     passwd='패스워드',
		     db='데이터베이스 이름',
		     charset='utf8');
```

#### 1.3.1 python 실습 코드 +
```python
# 1. MySQL 접속이 성공하면, Connection 객체로부터 cursor() 메서드를 호출하여 Cursor 객체를 가져옴
# 2. Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 전송
```

#### 1.3.2 테이블 생성하는 방법
```python
# 테이블 생성
# Cursor Object 가져오기 : cursor = db.cursor()
# SQL 실해하기 : cursor.execute(SQL)
# 실행 mysql 서버에 확정 반영하기 : db.commit()
cursor =  db.cursor(0
cursor

# cursor는 control structure of database 이다.(연결된 객체로 봐도 된다.)
sql = '''
   CREATE TABLE news(
      _id INT AUTO_INCREMENT,
      date VARCHAR(25) NOT NULL,
      company VARCHAR(15) NOT NULL,
      title VARCHAR(100) NOT NULL,
      content VARCHAR(3000) NOT NULL,
      PRIMRAY KEY(_id)
);
'''

# SQL 실행 ( Cursor 객체의 execute() 메서드를 사용하여 INSERT, UPDATE 혹은 DELETE 문장을 서버에 보냄)
cursor.execute(sql)

cursor.execute("SHOW TABLES")

# 삽입, 갱신, 삭제 등이 모두 끝났으면 Connection 객체의 commit() 메서드를 사용하여 데이터를 commit
db.commit()

# Connection 객체의 close() 메서드를 사영하여 DB 연결을 닫음
db.close()
```

#### 1.3.3 pymysql CREATE TABLE 코드 작성
```python
import pymysql

# 접속
db = pymysql.connect(host='ip',
                     port=3306,
		     user='유저이름',
		     passwd='비밀번호',
		     db='DB name',
		     charset='utf8')

# cursor 가져오기.
cursor = db.cursor()

# SQL 문 만들기
sql = ```
   CREATE TABLE korea2 (
       id INT UNSIGNED NOT NULL AUTO_INCREMENT,
       name VARCHAR(20) NOT NULL,
       model_num VARCHAR(10) NOT NULL,
       model_type VARCHAR(10) NOT NULL,
       PRIMARY KEY(id)
       );

# 실행하기
cursor.execute(sql)

# DB에 Complete 하기
db.commit()

# DB 연결 닫기
db.close()
```

#### 1.3.4 pymysql 다시 더 깔끔하게 작성하기.
```python
import pymysql

db = pymysql.connect(host='ip',
                     port=3306,
		     user='유저이름',
		     passwd='비밀번호',
		     db='DB NAME',
		     charset='utf8')

try:
    with db.cursor() as cursor:
       sql = '''
           CREATE TABLE korea(
	          id INT UNSIGNED NOT NULL AUTO_INCREMENT,
		  name VARCHAR(20) NOT NULL,
		  model_num VARCHAR(10) NOT NULL,
		  modeL_type VARCHAR(10) NOT NULL,
		  PRIMARY KEY(id)
		  );
       '''
       cursor.execute(sql)
       db.commit()
finally:
    db.close()
```

#### 1.4 python startwitdth() 는 str이 안에 존재하는지 아닌지 true, false 체크하는 함수

##### Description 
Python string method startwith() checks whether string starts with str, optionaly restricting the mathcing with the given indices start and end.

##### Syntax
Following is the syntax for startwith() method - 
```python
str.startwith(str, beg=0, end=len(string));
```

##### Parameters
* str - This is the string to be checked
beg - This is the optional parameter to set start index of the matching boundary.
* end - This is the optional parameter to end start index of the matiching boundary.


```python
str = "this is string example....wow!!!";

print str.startwith( 'this' )      # True
print str.startwith( 'is', 2, 4 )  # True
print str.startwith( 'this', 2, 4) # False
```

#### 1.5 pymysql에 데이터를 저장을 할때 PRIMARY KEY를 사용하지 않아도 되나?
PRIMARY KEY는 여러개의 TABLE이 존재하면 JOIN이나 다른 연산을 위해서 필요한 것이다.
잠시 잊고 있었다..ㅎㅎ


