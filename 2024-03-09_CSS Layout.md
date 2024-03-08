
# Box Model


content, padding, margin, border 등으로 표현되는 것


### box-sizing : border-box (시험에 나올지도)


기본값 content-box 기 때문에 width height 등이 content만 고려하기 때문에, css적용시 어려움이 많음 → border-box로 content가 아닌 border로서 고려한다.


# block 타입

- 항상 새로운 행
- width와 height 속성을 사용해 너비와 높이를 지정가능
- 기본적으로 width가 100%로 채워버림
- h1~6, p, div

# inline 타입 

- 새로운 행으로 나뉘지 않음
- width와 height속성을 사용할 수 없음
- 수직 방향
	- padding,margins, borders가 적용은 됨 but 다른 요소를 밀어낼 수는 없음
- 수평방향
	- 적용되고, 다른 요소도 밀어 낼 수 있다.
- a,img,span

# inline-block 


줄바꿈은 일어나지않지만, 너비와 높이를 조정하고 싶다 할때 사용


inline과 block요소 사이의 중간 지점을 제공하는 display 값


block 요소의 특징을 가짐 : width 및 height 속성 사용 가능 + padding, margin, border로 다른 요소 밀수 있음


### display: none : 공간조차 할당되지 않는다.


# Margin collapsing 마진 상쇄, 단답형


두 block 타입 요소의 margin top과 bottom이 만나 더 큰 margin으로 결합 됨


20 40 이라면 60이 아닌 40으로 합쳐짐


# CSS Position


각 요소의 위치와 크기를 조정하여 디자인 결정하는 것


display, position, float, flexbox 등


Normal Flow를 벗어나게 만드는 것


### position 유형 


static(기본)


### relative 

- 요소를 Normal Flow에 따라 배치
- 자기 자신을 기준으로 이동
- 요소가 차지하는 공간은 static일 때와 동일

### absolute

- 요소를 Normal Flow에서 제거
- 가장 가까운 relative 부모 요소를 기준으로 이동
- 문서에서 요소가 차지하는 공간이 없어짐

### fixed

- 요소를 Normal Flow에서 제거
- 현재 화면영역(viewport)을 기준으로 이동
- 문서에서 요소가 차지하는 공간이 없어짐

### sticky

- 요소를 Normal Flow에 따라 배치
- 요소가 일반적인 문서 흐름에 따라 배치되다가 스크롤이 특정 임계점에 도달하면 그 위치에서 고정(fixed)
- 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky 요소의 자리를 대체
	- 이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치기 때문

## z-index 정수값으로 겹치는 항목들에 순서를 지정 , 클수록 높은우선순위


# ⇒ Position이란? 


### 전체 페이지에 대한 레이아웃을 구성하는 것이 아닌 페이지 특정 항목의 위치를 조정하는 것


# axis 축


### main axis (주 축) 가로


flex item 들이 배치되는 기본 축


main start ~ main end 방향으로 배치 (기본 값)


### cross axis (교차 축) 세로


main axis에 수직인 축


cross start ~ cross end 방향으로 배치(기본 값)


# Flex Container


### 부모가 display : flex 또는 inline-flex 


→ 1차 자식 요소들이 flex item 이 됨

- flex 지정시 기본적으로 행(주 축의 기본값) 으로 나열되고 열로 한칸씩 늘어남

### flex-direction 방향 지정


row가 기본 값, column으로 지정할 경우 cross축으로 변경됨


-reverse 로 지정하면 시작선과 끝선이 서로 바뀐다.


### flex-wrap : flex item들이 한 행에 못 들어가고 넘칠 시 배치 여부 설정


nowrap 이 기본 값,  


### justify-content 주 축(가로)에 따른 flex item 과 주위에 공간 분배


### align-content 교차 축(세로)에 따라 flex item 과 주위에 공간 분배


flex-wrap 이 wrap 또는 wrap-reverse로 설정되야 가능


⇒ 한 줄 짜리 행에는 효과 없음 == nowrap이면 안된다.


### align-items : 교차 축을 따라 flex item 행을 정렬


### align-self : 교차 축을 따라 개별 flex item을 정렬


        ⇒ align-self는 부모의 영향을 받지 않음 


## Flexbox 속성

1. Flex Container 관련 속성
	1. display, flex-direction, flex-wrap, justify-content, align-items, align-content
2. Flex Item 관련 속성
	1. align-self, flex-grow, flex-basis, order

### flex-grow?  남은 행 여백을 비율에 따라 각 flex item에 분배 (시험에 나올 수도)

- item이 container 내에서 확장하는 비율을 지정
- ↔ flex-shrink

### flex-basis?  flex-item의 초기 크기 값을 지정


flex-basis와 width 값 중에 우선시 된다.


# 배치 : `flex-direction`, `flex-wrap`


# 공간 분배 : `justify-content`, `align-content`


# 정렬 : `align-items`, `align-self`


# CSS


### font 를 쓰기 위해서는 마지막에 글자체가 무조건 들어가 있어야 한다.


```css
font-weight : bold;
font-size : 18px
를 폰트로 줄이기 
font: bold 18px Arial, sans-serif; 
/* 글자체는 무조건 제일 마지막에 들어가야 한다. */
```

