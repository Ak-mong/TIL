
# Django Template System


데이터 표현을 제어하면서, 표현과 관련된 부분을 담당


### HTML  콘텐츠를 변수 값에 따라 바꾸고 싶다면


```python
# views,py
def index(request):
    context = {
        'name' : 'Alice'
    }
    return render(request, 'articles/index.html', context)
```


```html
<!--index.html-->
<body>
  <h1>안녕하세요 {{name}}님</h1>
</body>
```


# Django Template Language (DTL)


Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템


## DTL Syntax

1. Valiable 변수

	render 함수의 세번째 인자로 딕셔너리 데이터를 사용


	딕셔너리 key에 해당하는 문자열이 temmplate에서 사용가능한 변수명이 됨


	dot( . )를 사용하여 변수 속성에 접근할 수 있음


	HTML에 `{{valiable.attribute}}`

2. Filters

	표시할 변수를 수정할 때 사용 ( 변수 + ‘ | ’ + 필터)
	chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
	약 60개의 built-in template filters를 제공 ⇒ 외우는 것 아님


	`{[valiable|filter}}` `{{name|truncatewords:30}}

3. Tags

	반복 or 논리르 수행하여 제어 흐름을 만듦
	일부 태그는 시작과 종료 태그가 필요
	약 24개의 built-in templat tags를 제공


	`{% tag %}` `{% if %} {% endif%}`

4. Comments

	주석


	`<h1> Hello, {#name#} </h1>` 요소를 주석


	`{% comment %} ~~~~ {% endcomment %}` 줄 주석


### 예시


새로운 페이지를 만들기 위해서는 urls → views → templates 순으로 간다

1. 프로젝트의 [urls.py](http://urls.py/) 에서 dinner url 을 추가

	```python
	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('index/', views.index),
	    path('dinner/', views.dinner), # dinner 페이지 추가
	]
	```

2. 앱의 [views.py](http://views.py/) 에서 dinner 추가
변수를 여러 개를 만들었다면 이 변수를 다시 딕셔너리 형태로 묶어서 context를  만들어야 함

	```python
	def dinner(request):
	    foods = [
	        '국밥',
	        '국수',
	    ]
	    picked = random.choice(foods)
	    # 변수 두개를 만들었다면 두개를 다시 묶어줘야 함
	    context = {
	        'foods':foods,
	        'picked':picked,
	    }
	    return render(request, 'articles/dinner.html', context)
	```

3. HTML

	```html
	<body>
	  <p>{{picked}} 메뉴는 {{picked|length}}글자입니다.</p> <!-- 파이프라인 씀-->
	  <ul>
		  {% for food in foods %}
		    <li>{{food}}</li>
		  {% endfor %}
		</ul>
	  {% if foods|length == 0%}
	    <p>메뉴가 소진되었습니다.</p>  
	  {% else %}
	    <p>아직 메뉴가 남았습니다.</p>
	  {% endif %}
	</body>
	```


# 템플릿 상속


## 기본 텀플릿 구조의 한계


만약 모든 템플릿에 bootstrap을 적용하려면?


⇒ 모든 템플릿에 bootstrap CDN을 작성해야 할까?


## 템플릿 상속 Template inheritance

1. 페이지의 공통요소를 포함
2. 하위 템플릿이 재정의 할 수 있는 공간을 정의

하는 기본 ‘skeleton’템플릿을 작성하여 상속 구조를 구축


### 상속 구조를 위한 skeleton역할을 하게 되는 상위 템플릿 작성


```html
<!--base.html-->
<head>
  {% block style %}
  {% endblock style %}
</head>
<body>
  {% block content %}
  {% endblock content %}
</body>
```


### 기존 하위 템플릿의 변화


‘`extends`’ tag : 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림


### 반드시 1개만 템플릿 최상단에 작성되어야 함


```html
<!--index.html-->
{% extends "articles/base.html" %}
{% block content %}
  <h1>안녕하세요 {{name}}님</h1>
{% endblock content %}
```


> `block` tag  
> 하위 템플릿에서 재정의 할 수 있는 블록을 정의  
> (상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정하는 것  
> block 태그는 이름이 필요하다


```html
<!--base.html-->
<head>
  {% block style %}
  {% endblock style %}
</head>
<body>
  {% block content %}
  {% endblock content %}
</body>
```


# HTML form ( 요청과 응답)


## 데이터를 보내고 가져오기


HTML `form` element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기


HTML `form`은 HTTP 요청을 서버에 보내는 가장 편리한 방법


⇒ 실제 웹 서비스에서도 굉장히 많이 사용됨


## `form` element


사용자로부터 할당된 데이터를 서버에 전송


웹에서 사용자 정보를 입력하는 여러방식(text, password, checkbox 등)을 제공


input의 name 은 입력받은 값을 value로 name을 key값으로서 함께 서버로 보낼 때 사용됨


주소는 ? 을 기점으로 스타일이 바뀐다.


```html
<input type="text" id="message" name="message">
```


### 주소


`http://127.0.0.1:8000/search/?message=ssafy`
`https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=ssafy`
이 5가지의 데이터중 'ssafy'가 가장 중요하다
`https://search.naver.com/search.naver?query=ssafy` 라고만 쳐도 검색이 가능


⇒


```html
<form action="https://search.naver.com/search.naver">
  <label for="query">검색</label>
  <input type="text" id="query" name="query">
  <input type="submit"> <!-- 버튼으로 나오게 됨-->
</form>
```


## action & method 
- form의 핵심 속성 2가지
- 데이터를 어디(action)로 어떤 방식(method)으로 요청할지

- action
	- 입력 데이터가 전송될 URL을 지정(목적지)
	- 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
- method
	- 데이터를 어떤 방식으로 보낼 것인지 정의
	- 데이터의 HTTP request methods (GET, POST)를 지정

### 참고


get방식은 url 노출됨 ⇒ 로그인때는 쓰지 못함


⇒ 이 땐 post 방식 씀, 물론 이 이유만 있는 것은 아님


## `input` element


사용자의 데이터를 입력 받을 수 있는 요소


( type 속성 값에 따라 다양한 유형의 입력 데이터를 받음 )


## `name` attribute
- input의 핵심 속성

- 입력한 데이터에 붙이는 이름(key)

	⇒ 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음


## Query String Parameters

- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
- 문자열은 앰퍼샌드(’`&`’)로 연결된 key=value 쌍으로 구성되며,
- 기본 URL과는 물음표(’`?`’)로 구분됨
- 예시
	- http://host:port/path?key=value&key=value

### 경로 표기법은 OS 별로 다르기 때문에 주의해야한다.


‘C:// desktop/ssafy/aaaa → 리눅스 계열의OS


‘C:\\ desktop\ssafy\aaaa → 윈도우 계열의OS



# Form 활용하기


사용자 입력 데이터를 받아 그대로 출력하는 서버를 만들기 위해서는


view 함수가 몇 개가 필요할까?

1. throw 로직 작성

```html
<!--throw.html-->
<!--<form action="https://127.0.0.1:8000/catch/" method="GET">-->
<form action="/catch/" method="GET">
  <input type="text" name="message">
  <input type="submit"> <!-- 버튼으로 나오게 됨-->
</form>
```

1. catch 로직 작성

	throw 페이지에서 요청한 사용자 입력 데이터는 어떻게 가져와야 할까????


	************************************************


	## HTTP request 객체


	위에 catch.py에서 사용했음


	> request란?  
	> view 함수의 첫 번째 인자  
	> form으로 전송한 데이터 뿐만 아니라 모든 요청 관련 데이터가 담겨 있음


	![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/6c11cb66-a53e-4fd7-874a-0f891f1568ac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240313T165114Z&X-Amz-Expires=3600&X-Amz-Signature=0eec241ac3b130981dae412e2991e03e73f97d7a203c14b2c088f3ffff6d3206&X-Amz-SignedHeaders=host&x-id=GetObject)


	`request.Get` 하면 딕셔너리 형태의 데이터를 가져온다.


	`request.Get.get('key값')` : 딕셔너리의 Key으로  Value를 가져온다.


	```python
	# views.py
	def catch(request):
	    '''
	    throw 페이지에서 데이터를 받고
	    그 안에서 사용자 입력 데이터를 추출
	    템플릿에 그대로 출력'''
	    print(request) # <WSGIRequest: GET '/catch/?message=hello'>
	    print(type(request)) #<class 'django.core.handlers.wsgi.WSGIRequest'>
	    print(dir(request)) # 모든 명령어 나옴
	    print(request.GET) # <QueryDict: {'message': ['hello']}>
	    print(request.GET.get('message')) # hello
	    message = request.GET.get('message')
	    context = {
	        'message' : message
	    }
	    return render(request,'articles/catch.html',context)
	```


	```html
	<!-- catch.html -->
	<h2>{{message}}를 받았습니다!!!</h2>
	```


	************************************************


# 참고


## 추가 템플릿 경로 지정


템플릿 기본 경로 외 커스텀 경로 추가하기 - setting.py


```python
# 기본값
TEMPLATES = [
    {
        'DIRS': [],
    },
]
# 템플릿 경로 지정
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates',],
    },
]
```


```python
{% extends "templates/base.html" %}
=> {% extends "base.html" %} 로 바꿀수 있다.
```


### BASE_DIR 


settings에서 경로지정을 편하게 하기 위해 최상단 지점을 지정 해놓은 변수


`settings.py` - `BASE_DIR = Path(__file__).resolve().parent.parent`


[settings.py](http://settings.py/) 파일을 기준으로 두 단계 올라간다. (project폴더 → root폴더) 


## DTL 주의사항


연산은 view함수에서 하는거지 템플릿에서 하는 것이 아니다.

- Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 명칭만 동일
	- 절대 Python 코드로 실행되는것이 아님 == 파이썬과 관련 없음
- 프로그래밍적 로직이 아니라 표현을 위한 것임을 명심하기
- 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리할 것
- [https://docs.djangoproject.com/ko/4.2/ref/templates/builtins/](https://docs.djangoproject.com/ko/4.2/ref/templates/builtins/)

# Django URLs


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/1393c9f7-4182-4227-b3a5-449b1c8bdb7e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240313T165109Z&X-Amz-Expires=3600&X-Amz-Signature=99d895abd115363126b6b079b333549bb05d100c4012c1c6d15bc57348841c3d&X-Amz-SignedHeaders=host&x-id=GetObject)


# URL dispatcher (운항 관리자, 분재기)


URL 패턴을 정의하고, 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)


### 현재 URL 관리의 문제점


템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면 어떻게 해야???


⇒ 변하는 부분을 변수화 해야된다


### Valiable routing 


URL 일부에 변수를 포함 + 변수를 view  함수의 인자로 전달


`<path_converter:variable_name>` ex) `<int:num>` `<str:name>`


```html
path('articles/<int:num>/',views.detail)
path('hello/<str:name>/',views.greeting)
```


### path_converters 


URL 변수의 타입을 지정 (str, int 등 5가지 타입 지원)


```python
# urls.py
path('hello/<str:name>/', views.greeting),
```


```python
# views.py
def greeting(request, name): # 이 부분 중요
	context = {
	'name':name,
	}
	return render(request, 'articles/greeting.html', context)
```


### Trailing Slashes


무조건 URL 끝에 ‘`/`’ 을 붙어라, 


Django 는 무조건 붙어주지만, 다른 프레임워크가 이렇게 붙어줄지는 모르니 주의 해야함.

