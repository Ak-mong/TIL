
# Bootstrap Grid system 


웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템


## 목적: 반응형 웹


> 반응형 웹이란? 디바이스 종류나 화면 크기에 상관 없이, 어디서든 일관된 레이아웃및 사요ㅕㅇ자 경험을 제공하는 디자인 기술


### 왜 12개인가?


공약수의 개념에서 나누기 쉬운 수 이기 때문, 적당히 큰 수 중에서 나누기 쉬운 숫자이기 때문


## Grid system 기본 유소


margin, column, Gutter

1. Container
	- Column들을 담고 있는 공간
2. Column
	- 실제 컨텐츠를 포함하는 부분
3. Gutter
	- 컬럼과 컬럼 사이의 여백 영역
4. 1개의 row 안에 12개의 column 영역이 구성

# Grid System 기본


한 row의 col의 합을 12로 두는 것


### Nesting 중첩


col의 합이 12가 넘어 가는 순간 같은 row 안에서 밑 줄로 내려가버림, 이것을 이용해서 Nesting 씀


### Offset 상쇄 


offset으로 col을 대체해서 공백을 둘 수 있다


col과 offset이 같이 있다면, offset이 적용 후에 col이 적용됨


```css
4칸 채우고 / 4칸 비워지고 4칸 채우고
<div class="row">
  <div class="box col-4">col-4</div>
  <div class="box col-4 offset-4">col-4 offset-4</div>
</div>
```


## Gutter 


### 1. x축은 padding, y축은 margin으로 여백 생성
⇒ column끼리는 padding이지만 , row끼리는개별영역이기 때문에 margin을 줘야된다.


> `gx-0` 좌 우의 여백을 0으로 주겠다.   
> g : gutter, x : x축, -0 : 0 을 준다.


# 참고 : Grid System

- CSS가 아닌 편집 디자인에서 나온 개념, 구성 요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위함
- 기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인
- 정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여

# 반응형 웹


각 breakpoints 마다 설정된 최대 너비 값 이상으로 화면이 커지면 grid system 동작이 변경됨


### 6개의 분기점 xs(), sm(576px), md(768px), lg (992px), xl(1200), xxl


xs는 따로 값을 설정하지 않으면 기본 값


```css
<div class="box col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
	col
</div>
```


### offset 설정


반응형 웹 특징) 이전에 설정한 분기점의 내용이 남음


`col-sm-4 offset-sm-4` : sm-4 를 뒀기 때문에


`col-md-6 offset-md-0` : md-0로 초기화 해줘야됨


```css
<div class="row">
  <div class="box col-12 col-sm-4 col-md-6 ">
    col
  </div>
  <div class="box col-12 col-sm-4 col-md-6">
    col
  </div>
  <div class="box col-12 col-sm-4 col-md-6">
    col
  </div>
  <div class="box col-12 col-sm-4 offset-sm-4 col-md-6 offset-md-0">
    col
  </div>
</div>
```


### CSS에서 Media Query로 작성 할 경우


```css
@media (min-width: 576px){}
```


# Grid Card 


row에서 컨트롤 함, 하지만 offset은 해당 col에서 컨트롤 해야 한다.


```html
<div class="row row-cols-1 row-cols-sm-3 row-cols-md-2">
  <div class="col">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
          content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
  <div class="col">...</div>
  <div class="col">...</div>
  <div class="col offset-sm-4 offset-md-0">...</div>
</div>
 
```


# 종합 정리


그리드 시스템 > FlexBox > position 순으로 구식 기술


### 하지만


각각의 기술은 용도와 장단점이 있음


각 기술은 독립적인 용도를 가지지 않음,


어떤 기술이 적합한 도구가 될지는 특정 상황에 따라 다름


⇒ 이를 파악하기 위해 충분한 개별 경험이 필요

