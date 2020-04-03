# HTML 정리
* HTML5
* CSS (Cascading Style Sheets)
* JavaScript
  * D2Coding 설정 -> https://github.com /naver/d2codingfont
  

## 02_웹 페이지 기본 구조와 작성 방법

#### 1. html 태그의 lang 속성
  * ko, en, ja, ru, zh, de
  
#### 2. head 태그 내부에 넣을 수 있는 태그
  * meta : 웹 페이지에 추가 정보 전달
  * title : 페이지 제목 지정
  * script : 웹 페이지 스크립트 추가
  * link : 웹 페이지에 다른 파일 추가
  * style : 웹 페이지에 스타일시트 추가
  * base : 웹 페이지에 기본 경로 지정
 
 #### 3. 스타일 시트 작성과 실행
  * 내부 스타일 => HTML 페이지 내부에서 style 태그를 사용해 스타일 시트를 직접 입력, 스타일 시트가 짧은 경우
  * 외부 스타일 => 스타일 시트를 별도로 생성하고 link 태그의 href 속성을 사용해 불러옴, 협업 업무나 프로젝트 규모가 클 경우 사용

> style.css 를 외부에서 사용하는 방법
```html
<link rel="stylesheet" href="style.css">
```

#### 3.1 자바스크립트 작성과 실행
  * 내부 자바스크립트 => 위와 같이 내부에 작성
  * 외부 자바스크립트 => <script> 태그의 src 속성에 파일 경로를 입력해 HTML 페이지로 불러옴 

> script 내부 작성
```html
<script>
  alert('script 내부 작성 테스트')
</script>
```

> script 외부 작성
```html
<head>
  <script src="OuterJavaScript.js></script>
</head>
```

## 3장 HTML5 기본 태그
* 글자 태그 -> h1~h6 : 제목 글자 생성
* 목록 태그
 * p, br, hr : 본문 생성
 * a : 하이퍼링크 생성
 * b, i, small, sub, sup, ins, del : 글자 모양 지정
* 테이블 태그 
 * ul/ ol/ li : 순서가 없는/있는 목록 생성, 목록 요소 생성
* 미디어 태그
 * img, audio, video : 이미지, 오디오 , 비디오 삽입
 
 ### 3.1 제목과 본문 글자 태그
 #### 1. 제목 글자 : h = Heading : h1~h6
 #### 2. 본문 글자
  * p : 본문 문단 생성 
  * br : 줄 바꿈
  * hr : 수평 줄 삽입
  
#### 3. 하이퍼텍스트
 * 사용자의 선택에 따라 특정 정보로 이동하는 조직된 문서
 * a tag(Anchor): 다른 웹 페이지나 웹 페이지 내부의 특정 위치로 이동
 * Href : Hypyter Reference 를 의미한다.
```html
<a href="http://www.cu.ac.kr">대구가톨릭대학교</a>
```
#### 3.1 앵커 태그 4가지 경로
* 절대 경로
* 상대 경로
* 아이디 경로
 * #name - id 속성이 name인 태그의 위치로 이동
* 메일 경로
 * mailto : jaedeokhan@gmail.com -> 해당 주소로 메일 전송
 
 #### 3.1.3 웹 페이지 내부에 연결하기 -> id
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <a href="http://www.hanbit.co.kr">한빛미디어</a>
    <a href="http://www.naver.com">네이버</a>
    <a href="http://www.daum.com">다음</a>
    <a href="#alpha">Alpha 부문</a>
    <a href="#beta">Beta 부문</a>
    <a href="#gamma">Gamma 부문</a>
    <hr>
    <h1 id="alpha">Alpha</h1>
    <p>Lorem ipsum dolor sit amet</p>
    <h1 id="beta">Beta</h1>
    <p>Lorem ipsum dolor sit amet</p>
    <h1 id="gamma"></h1>
    <p>Lorem ipsum dolor sit amet</p>
</body>
</html>
```
 
#### 3.2.1 글자 모양 태그
* b : bold 
* i : italic
* small, sub(subscript) = 아래 첨자, sup(supscript) = 위 첨자, ins(insert) = 밑줄글자, del(delete) = 취소선이 그어진 글자


#### 3.2.2 내비게이션 메뉴 
* 웹 사이트의 다른 웹 페이지로 이동할 수 있는 버튼
* ul : 순서가 없는 목록 unordered list 생성
* ol : 순서가 있는 목록 ordered list 생성
* li : 목록 요소 list item 생성

#### 3.2.3 테이블 태그
* table : 표 삽입
* tr(table row) : 표에 행 삽입
* th(table heading) : 표의 제목 셀 생성
* td(table data) 표의 일반 셀 생성

> 시간표 만들기 -> table의 border은 겉의 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table border="10">
        <thead>
            <tr>
                <th></th>
                <th>월</th>
                <th>화</th>
                <th>수</th>
                <th>목</th>
                <th>금</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1교시</td>
                <td>영어</td>
                <td>국어</td>
                <td>과학</td>
                <td>미술</td>
                <td>기술</td>
            </tr>
            <tr>
                <td>2교시</td>
                <td>도덕</td>
                <td>체육</td>
                <td>영어</td>
                <td>수학</td>
                <td>사회</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
```

#### 3.2.4 테이블 태그의 속성
* table - border : 표의 테두리 두께 지정
* th,td 
 * colspan : 셀의 너비 지정
 * rowspan : 셀의 높이 지정

> 행.열 병합 표 생성 -> colspan 속성과 rowspan 속성을 적용
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table border="1">
        <tr>
            <th colspan="2">지역별 홍차</th>
        </tr>
        <tr>
            <th rowspan="3">중국</th>
            <th>정산소종</th>
        </tr>
        <tr><td>기문</td></tr>
        <tr><td>운남</td></tr>
        <tr>
            <th rowspan="4">인도 및 스리랑카</th>
            <td>아삼</td>
        </tr>
        <tr><td>실론</td></tr>
        <tr><td>다질링</td></tr>
        <tr><td>닐기리</td></tr>
    </table>
</body>
</html>
```

#### 4. 미디어 태그
* 이미지, 오디오, 비디오 등 멀티미디어 넣을 때 사용

#### 4.1 미디어 태그 구분
* 내용물을 가질 수 있는 태그 -> <audio></audio>, <video></video>
* 내용물을 가질 수 없는 태그 -> <img>

#### 4.1.1 미디어 태그 속성 
* img 태그 
 * src : 이미지 경로 지정
 * alt : 이미지가 없을 대 나오는 글자 지정
 * width : 이미지의 너비 지정
 * height : 이미지의 높이 짖어

* audio, video 태그
 * src : 음악, 비디오 파일의 경로 지정
 * preload : 음악, 비디오 준비 중일 때 데이터를 모두 불러올지 여부 지정
 * autoplay : 음악, 비디오의 자동 재생 여부 지정
 * loop : 음악, 비디오의 반복 여부 지정
 * controls : 음악, 비디오의 재생 도구 출력 여부 지정
 
* video 태그
 * width : 비디오의 너비 지정
 * height : 비디오의 높이 지정
 
> 기본 예제 3-9 : 멀티미디어(이미지, 오디오, 비디오) 삽입
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <img src="http://www.hanbit.co.kr/images/common/logo_hanbit.png" alt="펭귄" width="300">
    <br>
    <img src="Noting" alt="그림이 존재하지 않습니다." width="300">
</body>
</html>
```
  
> 음악 파일 준비: 준비 파일(오디오.mp3)을 HTML 페이지와 같은 폴더에 넣기.
```html
<body>
 <audio src='이름.mp3' controls='controls'></audio>
</body>
```


 
  
  
  
  
  
  
  
  
  
  
  
 
 
 

