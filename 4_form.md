## 2020 04 08 WED - 4장 HTML5 입력 양식 태그와 구조화 태그

### 데이터 전달 방식
* GET : 주소에 파라미터를 날려서 사용한다 -> 구글 검색엔진
* POST  : 주소에 보여주지 않는다. 비밀스럽게! 보안 관련

#### <form>태그는 method 속성의 방식으로 action 속성 장소에 데이터 전달
* action : 데이터를 전달할 목적지
```html
<form action="전송 위치" method="전송 방식"></form>
```

```html
    <form method="get">
        <input type="text" name="search">
        <input type="submit">
    </form>
    <form method="post">
        <input type="text" name="search">
        <input type="submit">
    </form>
```

#### [기본 예제 4-1]기본 입력 양식 태그
```html
    <form>
        <!-- 사용자가 입력하는 입력 양식 -->
        <input type="text" name="text" value="text"><br>
        <input type="password" name="password" value="password"><br>
        <input type="file" name="file" value="file"><br>
        <input type="checkbox" name="checkbox" value="checkbox"><br>
        <input type="radio" name="radio" value="radio"><br>
        
        <!-- 보이지 않는 입력 양식 -->
        <input type="hidden" name="hidden" value="hidden"><br>

        <!-- 버튼 -->
        <input type="button" value="button"><br>
        <input type="reset" value="reset"><br>
        <input type="submit" value="submit"><br>
        <input type="image" src="http://placehold.it/100x100"><br>
    </form>
```

#### [기본 예제 4-2] 간단한 입력 양식 생성 -> 라디오 버튼 name 속성을 이용해서 여러 대상 중 하나만 선택하는 형태
* radio 버튼은 name 속성을 같게 입력해야 여러 항목 중 하나만 선택이 된다.
```html
    <form>
        <table>
            <tr>
                <td><label for="username">이름</label></td>
                <td><input id="username" type="text" name="username"></td>
            </tr>
            <tr>
                <td>성별</td>
                <td>
                    <input id="man" type="radio" name="gender" value="m">
                    <label for="man">남자</label>
                    <input id="woman" type="radio" name="gender" value="w">
                    <label for="woman">여자</label>
                </td>
            </tr>
        </table>
        <input type="submit" value="가입">
    </form>
```

#### [기본 예제 4-3] 선택 가능한 입력 양식
1. 한 항목만 선택하기 : <select> 태그 이용
  * 목록으로 보여 주는 항목 중 하나 또는 여러 개를 선택할 때 사용
  * 기본적으로 하나만 선택가능
  * <optgroup> , <option> 태그를 함께 사용
> form_selectBasic.html
```html
<body>
    <select>
        <option>김밥</option>
        <option>떡볶이</option>
        <option>순대</option>
        <option>어묵</option>
    </select>
</body>
```

2. 여러 항목 선택하기 : <select> 태그의 multiple 속성 
> form_selectMulti.html
```html
<body>
    <select multiple="multiple">
        <option>김밥</option>
        <option>떡볶이</option>
        <option>순대</option>
        <option>어묵</option>
    </select>
</body>
```

3. 선택 옵션 묶기 : <optgroup> 태그 사용
> form_selectGroup.html
```html
<body>
    <select>
        <optgroup label="HTML5">
            <option>Multimedia Tag</option>
            <option>Connectivity</option>
            <option>Device Access</option>
        </optgroup>
        <optgroup label="CSS3">
            <option>Animation</option>
            <option>3D Transform</option>
        </optgroup>
    </select>
</body>
```

#### [기본 예제 4-4] 연관 있는 입력 양식 그룹으로 묶기
* fieldset 태그, legend 태그
> form_group.html
```html
    <form>
        <fieldset>
            <legend>입력 양식</legend>
            <table>
                <tr>
                    <td><label for="name">이름</label></td>
                    <td><input id="name" type="text"></td>
                </tr>
                <tr>
                    <td><label for="mail">이메일</label></td>
                    <td><input id="mail" type="email"></td>
                </tr>
            </table>
            <input type="submit">
        </fieldset>
    </form>
```

#### 공간 분할 태그
* css로 원하는 레이아웃을 구성하기 위해 공간 분할

#### HTML5의 대표적인 공간 분할 태그? -> <div> , <span>
* div : 블록 형식으로 공간 분할
* span : 인라인 형식으로 공간 분할

#### 1. 공간을 블록 형식으로 분할하기.
> space_block.html
```html
<body>
    <div>div 태그 - block 형식</div>
    <div>div 태그 - block 형식</div>
    <div>div 태그 - block 형식</div>
    <div>div 태그 - block 형식</div>
    <div>div 태그 - block 형식</div>
</body>
```

#### 2. 공간을 인라인 형식으로 분할하기
* 자신의 글자 크기만큼 영역 차지
* 왼쪽에서 오른쪽으로 쌓임
> space_inline.html
```html
<body>
    <span>span 태그 - inline 형식</span>
    <span>span 태그 - inline 형식</span>
    <span>span 태그 - inline 형식</span>
    <span>span 태그 - inline 형식</span>
    <span>span 태그 - inline 형식</span>
    <p>p 태그 - block 형식</p>
    <p>p 태그 - block 형식</p>
</body>
```

#### 시맨틱 태그
* 시맨틱 웹
  * 특정 태그에 의미르르 부여한 웹
  * 프로그램이 코드를 읽고 의미를 인식할 수 있는 지능형 웹

#### HTML5 시맨틱 태그
1. header : 머리말(페이지 제목 , 페이지 소개)
2. nav : 하이퍼링크들을 모아 둔 내비게이션
3. aside : 본문 흐름에 벗어나는 노트나 팁
4. section : 문서의 장이나 절에 해당하는 내용
5. article : 본문과 독립적인 콘텐츠 영역
6. footer : 꼬리말(저자나 저작권 정보)

#### [기본 예제 4-6] 시맨틱 태그를 이용한 레이아웃 구성
> space_semantic.html
```html
<body>
    <header>
        <h1>HTML5 기본</h1>
    </header>
    <nav>
        <ul>
            <li><a href="">메뉴 - 1</a></li>
            <li><a href="">메뉴 - 2</a></li>
            <li><a href="">메뉴 - 3</a></li>
        </ul>
    </nav>
    <section>
        <article>
            <h1>Lorem ipsum dolor sit amet</h1>
            <p>Lorem ipsum dolor sit amet, consect</p>
        </article>
        <article>
            <h1>ipsum dolor sit amet</h1>
            <p>sum dolor s</p>
        </article>
    </section>
    <footer>
        <address>대구광역시 달서구 상인동</address>
    </footer>
</body>
```







