### 2020 0503 SUN 
### Ec2 Ubuntu 18.04 에서 mysql 설치 후 연동해서 사용하기.

#### 1. Ec2 Ubuntu 18.04 instance create
보안그룹 자신의 ssh , mysql 열어주기.

#### 2. apt update & mysql install & user config

#### 2.1 apt update & mysql install
```bash
$ sudo apt update
$ sudo apt install mysql-server
$ sudo systemctl status mysql
```

#### 2.2 mysql 설정
```bash
# 이것을 통해서 mysql을 설정한다(비밀번호 등)
$ sudo mysql_secure_installation

$ sudo mysql -u root -p
mysql> show databases;
```

#### 2.3 mysql 계정 추가 및 권한 부여하기.
```bash
# 1. 사용자 계정을 추가하기.
# '%' 는 기존에 'localhost'와는 달리 다른 시스템에서 외부로 접근이 가능하게 하는것이다. 즉 외부에서 접근을 가능하게 하는 것이다.
$ create user '(사용자 계정명)'@'%' identified by '(비밀번호)';
$ create database (데이터베이스이름);

# 2. Root 계정으로 해당 사용자에게 권한을 부여하기.
$ grant all privileges on (데이터베이스명칭).* to '(사용자계정명)'@'%';

# 2.1 lab 데이터베이스에 목록이 추가된것을 확인하기.
$ show databases;
```

#### 3. mysql database utf-8 config
```bash
# 1.
$ vim /etc/mysql/my.cnf

# 아래의 내용들을 추가
[client]
default-character-set=utf8

[mysql]
default-character-set=utf8


[mysqld]
collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'
character-set-server = utf8

# 2. 
$ mysql -p -u root 
mysql> alter database 데이터베이스이름 default character set utf8;

$ sudo systemctl restart mysql

# 위 설정 전 테이블을 생성하였다면 테이블(예, 고객) 캐릭터셋을 다음과 같이 변경
$ mysql -p -u user mydb
mysql> alter table 고객 convert to character set utf8;
```

#### 4. 외부에서 Ec2 mysql 을 접근을 할려면, Ec2 Instacne 에서 bind-address 설정을 해당 아이피를 허용하거나 모든 ip를 허용해 줘야한다.

* vim /etc/mysql/mysql.conf.d/mysqld.cnf

```bash
# OperationalError: (2003, "Can't connect to MySQL server on '54.84.72.175'
#([WinError 10061] 대상 컴퓨터에서 연결을 거부했으므로 연결하지 못했습니다)")
# 위와 같은 에러가 나타난다.

bind-address = 0.0.0.0 # 변경을 하면 모든 곳에서 접근이 가능하다.
# 0.0.0.0 == * == ::
```
