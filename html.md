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

