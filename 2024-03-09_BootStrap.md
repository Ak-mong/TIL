
# BootStrap


css 프론트엔드 프레임워크 (Toolkit: 도구 상자)


트위터에서 만들어짐


[https://getbootstrap.com/](https://getbootstrap.com/) 외국사이트에 비해 한국 사이트는 버젼이 뒤쳐짐


# CDN : content Delivery Network

- 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술
- 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화 ( 웹 페이지 로드 속도를 높임)
- 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

### Bootstrap CDN : 파일로서 저장해서 사용하는 것


## 기본사용법


```css
<p class= "mt-5"> Hello, world!</p>
m            t   -   5
{property}{sides}-{size}
```


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/1df2f7c9-2514-47ff-917f-f2a55799f9ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240308T163534Z&X-Amz-Expires=3600&X-Amz-Signature=b946f53e50c852ca25a1bc5bf288b321fbfda4454dd475714a2957d9a884ff2d&X-Amz-SignedHeaders=host&x-id=GetObject)


## Reset CSS


모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트


⇒ HTML Element, Table, List 등의 요소들에 일관성 있게 스타일을 적용 시키는 기본 단계


user agent stylesheet가 브라우저마다 상이함 ⇒ 모두 똑같은 스타일 상태로 만들고 스타일 개발을 시작하자


> User-agent stylesheets 모든 문서에 기본 스타일을 제공하는 기본 스타일 시트


### Normalize CSS


Reset CSS 방법 중 대표적인 방법


웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정하는 방법

- 경우에 따라 IE 또는 EDGE 브라우저는 표준에 따라 수정할 수 없는 경우도 있는데, 이 경우 IE 또는 EDGE의 스타일을 나머지 브라우저에 적용시킴

### 부트스트랩에서는 Reset CSS


`bootstrap-reboot.css`라는 파일명으로 자체적으로 커스텀해서 사용하고 있음


# Bootstrap 활용


## Typography 
제목, 본문, 텍스트, 목록 등


### Display headings


기본 heading보다 더 눈에 띄는 제목이 필요할 경우 (더 크고 약간 다른 스타일)


`<h1 class="display-1"> Display 1 </h1>`


### Inline text elements


HTML inline 요소에 대한 스타일


```css
<p>You can use the mark tag to <mark>highlight</mark> text.</p>
<p><del>This line of text is meant to be treated as deleted text.</del></p>
<p><s>This line of text is meant to be treated as no longer accurate.</s></p>
<p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
<p><u>This line of text will render as underlined.</u></p>
<p><small>This line of text is meant to be treated as fine print.</small></p>
<p><strong>This line rendered as bold text.</strong></p>
<p><em>This line rendered as italicized text.</em></p>
```


### Lists


HTML list 요소에 대한 스타일


```css
<ul class="list-unstyled">
  <li>This is a list.</li>
  <li>It appears completely unstyled.</li>
  <li>Structurally, it's still a list.</li>
  <li>However, this style only applies to immediate child elements.</li>
  <li>Nested lists:
    <ul>
      <li>are unaffected by this style</li>
      <li>will still show a bullet</li>
      <li>and have appropriate left margin</li>
    </ul>
  </li>
  <li>This may still come in handy in some situations.</li>
</ul>
```


## Colors


### Bootstrap Color system 부트스트랩이 지정하고 제공하는 색상 시스템


색상 키워드를 가지고 적용한다


```css
<div class="text-bg-primary p-3">Primary with contrasting color</div>
<div class="text-bg-secondary p-3">Secondary with contrasting color</div>
<div class="text-bg-success p-3">Success with contrasting color</div>
<div class="text-bg-danger p-3">Danger with contrasting color</div>
<div class="text-bg-warning p-3">Warning with contrasting color</div>
<div class="text-bg-info p-3">Info with contrasting color</div>
<div class="text-bg-light p-3">Light with contrasting color</div>
<div class="text-bg-dark p-3">Dark with contrasting color</div>
```


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/e90b467d-25d6-401d-a678-d0a161495fe7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240308T163534Z&X-Amz-Expires=3600&X-Amz-Signature=2e387bd42790efc42d14455a95f0f5d05dd232adf85a46840ba5a07bfe084c0f&X-Amz-SignedHeaders=host&x-id=GetObject)


### border


```html
<span class="border border-primary"></span>
<span class="border border-primary-subtle"></span>
```


# Component
Bootstrap에서 제공하는 UI 관련 요소


### 버튼, 네비게이션 바, 카드, 폼, 드롭다운 등 이 있다


### 이점


일관된 디자인을 제공하여 웹 사이트의 구성 요소를 구축하는 데 유용하게 활용


## Alert


```html
<div class="alert alert-primary" role="alert">
  A simple primary alert—check it out!
</div>
```


### Badges 
`<h1>Example heading <span class="badge text-bg-secondary">New</span></h1>``


### Buttons
`<button type="button" class="btn">Base class</button>`


### Cards



```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```


### Navbar
[https://getbootstrap.com/docs/5.3/components/navbar/](https://getbootstrap.com/docs/5.3/components/navbar/)


# 왜 Bootstrap을 사용하는 가?

1. 가장 많이 사용되는 CSS 프레임워크
2. 사전에 디자인된 다양한 컴포넌트 및 기능
	1. 빠른 개발과 유지보수가 가능하다
3. 손쉬운 반응형 웹 디자인 구현
4. 커스터마이징이 용이
5. 크로스 브라우징 지원
	1. 모든 주요 브라우저에서 작동하도록 설계되어 있음

### carousel 회전목마 : 슬라이딩 메인사진 같은것


같은 id값을 가지고 여러개를 만들 때 제대로된 작동이 되지 않음


⇒ carousel 의 id 값과 각 버튼의 data-s-target이 일치 하는 지를 잘 봐야 한다.


### modal


modal id 값과 버튼의 data-bs-target이 각각 올바르게 일치하는 지 확인

1. modal 코드와 button 코드가 반드시 함께 다녀야할까? 상관없음, data-bs-target이 중요하다.
2. modal 코드가 다른 코드 안쪽에 중첩되어 들어가버리면 modal이 켜졌을때 회색 화면 뒤로 감춰질 수 있다
3. modal 코드는 주로 body 태그가 닫히는 곳에 모아두는 것을 권장

# Semantic Web


웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식


이 요소가 시각적으로 어떻게 보여질까? ⇒ 이 요소가 가진 목적과 역할은 무엇일까? 의 흐름


### Semantic in HTML
HTML 요소가 의미를 가진다는 것


`<p style="font-size: 30px;"> Heading </p>` 단순히 제목처럼 보이게 큰글자로 만드는 것


→ 


`<h1> Heading </h1>` ”페이지 내 최상위 제목” 이라는 의미를 제공하는 요소 h1


	⇒ 브라우저에 의해 스타일이 지정됨


== 차이가 있다


### HTML Semantic Element


기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소


⇒ 검색엔진 및 개발자가 웹 페이지 콘텐츠를 이해하기 쉽도록 하기 위함


대부분의 개발자들이 `div` 태그만 사용하게 되면서 스크린 리더가 어느 부분이 무엇을 뜻하는지를 알 수 없게 되버렸음 


### ⇒ 같은 기능을 가지고 있지만, 이름은 다른 태그를 만듬으로 의미를 부여시킴


### 대표적인 Semantic Element ( div와 같은 기능 가짐 )

- header
- nav
- main
- article
- section
- aside
- footer

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/6d0785e1-2c13-4fcc-b3c0-d92eece336d1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240308T163534Z&X-Amz-Expires=3600&X-Amz-Signature=345e04eb5a37ec503ec1ee2e51c7eb348e020050f202a010d88170f5e07f7340&X-Amz-SignedHeaders=host&x-id=GetObject)


## Semantic in CSS


### CSS 방법론 : CSS를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인


# OOCSS : Object Oriented CSS


객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론


## OOCSS 기본 원칙

1. 구조와 스킨을 분리
2. 컨테이너와 콘텐츠를 분리

### 1. 구조와 스킨 분리 


-1) 구조와 스킨을 분리함으로써 재사용 기능성을 높임


-2) 모든 버튼의 공통 구조를 정의 + 각각의 스킨(배경색과 폰트 색상)을 정의


```css
/* bad */
.blue-button{
  border: none;
  font-size: 1em;
  padding: 10px 20px;
  background-color: blue;
  columns: white;
}
```


```css
/* good */
.button{
  border:none;
  font-size: 1em;
  padding: 10px 20px;
}
.button-blue{
  background-color: blue;
  color: white;
}
.button-red{
  background-color: red;
  color: white;
}
```


### 2. 컨테이너와 콘텐츠 분리

- 객체에 직접 적용하는 대신 객체를 둘러싸는 컨테이너에 스타일을 적용
- 스타일을 정의할 때 위치에 의존적인 스타일을 사용하지 않도록 함
- 콘텐츠를 다른 컨테이너로 이동시키거나 재배치할 때 스타일이 깨지는 것을 방지

### OOCSS 적용 예시


```html
/* bad */
.header h2{
  font-size:24px;
  color:white;
}
.footer h2{
  font-size: 24px;
  color: black;
}


```

- 변경 전
	- .header와 .footer 클래스가 폰트 크기에 색 둘 다 영향을 주고 있음

```css
/* good */
.container .title{
  font-size:24px;
}
.header{
  color:white;

}
.footer{
  color:black;
}
```

- 변경 후
	- .container .title은 폰트 크기 담당 ( 콘텐츠 스타일)
	- .header와 .footer는 폰트 색 담당 ( 컨테이너 스타일)

# 참고


## 책임과 역할


### HTML : 콘텐츠의 구조와 의미
CSS : 레이아웃과 디자인


## 의미론적인 마크업이 필요한 이유

- 검색엔진 최적화 (SEO)
	- 검색 엔진이 해당 웹 사이트를 분석하기 쉽게 만들어 검색 순위에 영향을 줌
- 웹 접근성(Web Accessibility)
	- 웹 사이트, 도구, 기술이 고령자나 장애를 가진 사용자들이 사용할 수 있도록 설계 및 개발하는 것
	- ex) 스크린 리더를 통해 전맹 시각장애 사용자에게 웹의 글씨를 읽어줌
	- https://nuli.navercorp.com
