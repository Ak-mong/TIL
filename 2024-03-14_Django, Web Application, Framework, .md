
### Web application ( web service) 개발


인터넷을 통해 사용자에게 제공되는 소프트웨어 프로그램을 구축하는 과정


다양한 디바이스에서 웹 브라우저를 통해 접근하고 사용할 수 있음


## 웹은 어떻게 동작할까?


클라이언트-서버 구조 : 클라이언트가 요청(requests)하고 서버가 반응(response)한다


### Client 클라이언트 


서비스를 요청하는 주체 ( 웹 사용자의 인터넷이 연결된 장치, 웹 브라우저)


### Server 서버


클라이언트의 요청에 응답하는 주체 ( 웹 페이지, 앱을 저장하는 컴퓨터)


### 웹 페이지를 보게 되는 과정

1. 웹 브라우저(클라이언트)에서 ‘google.com’을 입력
2. 브라우저는 구글 컴퓨터(서버)에게 ‘Google 홈페이지.html’ 파일을 달라고 요청
3. 요청을 받은 구글 컴퓨터는 데이터베이스에서 파일을 찾아서 응답
4. 전달 받은 파일을 사람이 볼 수 있도록 웹 브라우저가 해석해주면서 사용자가 구글의 메인페이지를 보게 됨

## 웹 개발에서의 Frontend 와 Backend


### Frontend ( 프론트엔드 )

- 사용자 인터페이스 (UI)를 구성하고, 사용자가 애플리케이션과 상호작용할 수 있도록 함
- HTML, CSS, JavaScript, 프론트엔드 프레임워크 등

### Backend ( 백엔드 )

- 서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용을 담당
- 서버 언어(Python, Java 등) 및 백엔드 프레임워크, 데이터베이스, API, 보안 등

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/16bdbfb9-ff5e-4bf2-bcd2-24a052d8f21c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240313T162230Z&X-Amz-Expires=3600&X-Amz-Signature=e3cffa67a434a4ecbddf4530bb4858afd04855b3ab223cb72a4094e0989f7da6&X-Amz-SignedHeaders=host&x-id=GetObject)


# Framework


잘 만들어진 것들을 가져와 좋은 환경에서 내 것으로 잘 사용하는 것도 능력인 시대


개발에 필요한 기본구조, 규칙, 라이브러리 등을 제공


> 거인의 어깨 위에서 프로그래밍하기


# django 


Python 기반의 대표적인 웹 프레임워크


다양성, 확장성, 보안, 커뮤니티 지원 등의 장점이 있다.


> 이 중 커뮤니티 지원이 가장 주요한 장점  
> 아무리 좋은 기술이라도 커뮤니티보다는 좋지 않다.


spotify, instagram, dropbox 등 다양한 곳에서 하나의 기술로서 사용한다.


# Django를 사용해서 서버를 구현할 것


# 가상환경


Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 독립적인 실행 환경


pip install 을 통해 다운로드하면 global환경에서 다운받게 됨, ⇒ 독립적인 실행환경이 아니게 됨


> 만약? 한 개발자가 2개의 프로젝트를 진행해야 되는데, 패키지 버젼을 다르게 사용해야 한다.


하지만 파이썬 환경에서는 패키지는 1개의 버젼만 존재할 수 있다.


⇒ 다른 패키지 버젼 사용을 위한 독립적인 개발 환경이 필요하다.


> 만약? 함께 사용하면 충돌이 발생하는 패키지를 각 프로젝트에서 진행해야된다면?


⇒ 독립적인 개발 환경이 필요하다.


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/671f836c-1107-4b0f-b782-f220746bff28/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240313T162230Z&X-Amz-Expires=3600&X-Amz-Signature=9ea1330cdeef2417d18887dca118562b55fffd6fa1d5aa0381d5e70fbf85a017&X-Amz-SignedHeaders=host&x-id=GetObject)

1. 가상환경 venv 생성 `python  -m    venv     venv` : venv 라는 이름의 가상환경을 만들겠다.

	아무것도 설정되있지 않은 환경을 만듬

2. 가상 환경 활성화 `source venv/Scripts/activate`
’on 했다’ 라고 표현할 수 있음
환경에 들어간다는 개념이 아닌 가상환경을 켰다 껏다 하는 개념
3. 환경에 설치된 패키지 목록 확인 `pip list`
가상환경을 처음 만들었으면 pip와 setuptools만 존재한다.

	> 패키지 목록이 왜 필요한가? 만약 두명의 개발자가 하나의 프로젝트를 함께 개발한다고 할 때?


	기본적으로 가상환경은 github에 올리지 않음


	팀원 A가 어떤 패키지를 설치했고, 어떤 버젼을 설치했는지 A의 가상환경 상황을 알수 X


	⇒ 가상 환경에 대한 정보, 즉 패키지 목록이 공유되어야 한다.


	### 의존성 패키지

	- 한 소프트웨어 패키지가 다른 패키지의 기능이나 코드르 사용하기 떄문에 그 패키지가 존재해야만 제대로 작동하는 관계
	- 사용하려는 패키지가 설치되지 않았거나, 호환되는 버젼이 아니면 오류가 발생하거나 예상치 못한 동작을 보일 수 있음
	- jupyter notebook의 의존성이 굉장히 어지럽다.
4. 의존성 패키지 목록 설정 `pip freeze > requirements.txt`
텍스트 파일로 패키지 목록을 저장해주는 명령어
requirments.txt 는 단순한 이름이지만, 다른이름으로 하지않음, venv도 마찬가지
5. 의존성 패키지 설치 시 `pip install -r requirements.txt` 를 통해 패키지 바로 설치 가능

> 주의사항

1. venv 폴더 안의 내용을 직접적으로 건드리면 안된다.
2. 의존성 : 하나의 패키지를 설치하면 하나만 설치되는것이 아님, 그런데 하나의 패키지가 업그레이드 될 때 의존하고 있는 다른 패캐지와 관계가 깨질 수도 있어서, 문제가 발생할 수도 있다

	⇒ 패키지와 그 버젼을 정확히 관리하는 것이 중요하다.


### ⇒ 가상 환경 & 의존성 패키지 관리


# Django

1. 장고 설치 `pip install django`
2. Django 프로젝트 생성 `django-admin startproject firstpjt .` firstpjt 라는 이름의 프로젝트 생성
3. Django 서버 실행 `python` [`manage.py`](http://manage.py/) `runserver` manage.py와 동일한 경로에서 진행

### 만약 git과 Django 프로젝트 생성 루틴 정리 

1. 가상 환경 생성
2. 가상 환경 활성화
3. 의존성 파일 생성(패키지 설치시마다 진행)
4. .gitignore 파일 생성 (첫 add 전)  대부분[gitignore.io](http://gitignore.io/) 에서 생성
5. git 저장소 생성
6. Django 프로젝트 생성

> 왜 가상환경을 사용하는 가?  
> 1. 의존성 관리 : 라이브러리 및 패캐지를 각 프로젝트마다 독립적으로 사용 가능  
> 2. 팀 프로젝트 협업 : 모든 팀원이 동일한 환경과 의존성 위에서 작업하여 버전간 충돌을 방지


### LTS (Long-Term Support) 란?

- 안정적인 버전을 의미
- 대규모 단위에서는 소프트웨어 업그레이드에 많은 비용과 시간 필요 ⇒ 안정적이고 장기간지원해야함

### Django 는 Full Stack framework인가요?


일단 Yes, 하지만 , 프론트에서는 다른 것들에 비해 매우 미흡함, 그래서 Backend에 속한다고 볼 수 있다.


# Django Design Pattern 디자인 패턴


소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책


(공통적인 문제를 해결하는 데 쓰이는 형식화 된 관행)


⇒ 애플리케이션의 구조는 이렇게 구성하자 라는 관행


### MVC 디자인 패턴 


Model, View, Controller


controller는 model과 view를 연결하는 역할


애플리케이션을 구조화하는 대표적인 패턴 


( ‘데이터’ & ‘사용자 인터페이스’ & “비즈니스 로직”을 분리


시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위해


### MTV 디자인 패턴 ( Django가 MVC를 부르는 이름)


Model, Template, View


MVC 의 View → Template


MVC 의  Controller → View


Django 에서 애플리케이션을 구조화하는 패턴 


⇒ (기존 MVC 패턴과 동일하나 단순히 명칭을 다르게 정의)


## 프로젝트와 앱


하나의 프로젝트에 여러 개의 앱 


기능 별로 앱을 나누는 것이 일반적


### Django project 애플리케이션의 집합


DB 설정, URL 연결, 전체 앱 설정 등을 처리


### Django application 독립적으로 작동하는 기능 단위 모듈


각자 특정한 기능을 담당하며 다른 앱들과 함꼐 하나의 프로젝트를 구성


### 만약 온라인 커뮤니티 카페를 만든다면?


프로젝트 : 카페 (전체 설정 담당)


앱 : 게시글, 댓글, 회원 관리 등 (DB, 인증, 화면)


### 앱을 사용하기 위한 순서


반드시 이 순서로 이루어져야 한다.

1. 앱 생성
2. 앱 등록

### 1. 앱 생성 `python` [`manage.py`](http://manage.py/) `startapp articles`


앱의 이름은 “복수형”으로 지정하는 것을 권장, articles 는 단순한 앱 이름


물리적으로 프로젝트 밖에 articles폴더가 생김, ⇒ 등록하는 절차 필요


### 2. 앱 등록


```python
#settings.py
INSTALLED_APPS = [
    'articles', # 추가
    ...
]
```


## 프로젝트 구조

- [`settings.py`](http://settings.py/) : 프로젝트의 모든 설정을 관리
- [`urls.py`](http://urls.py/) : 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결

⇒  이 둘은 수업과정에서 수정할 수도 있음

- `__init__.py` : 해당 폴더를 패키지로 인식하도록 설정하는 파일
- [`asgi.py`](http://asgi.py/) : 비동기식 웹 서버와의 연결 관련 설정
- [`wsgi.py`](http://wsgi.py/) : 웹 서버와의 연결 관련 설정
- [`manage.py`](http://manage.py/) : Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

⇒ 수업과정에서 수정할 일 없음


## 앱 구조

- [`admin.py`](http://admin.py/) : 관리자용 페이지 설정
- [`models.py`](http://models.py/) DB와 관련된 Model을 정의

	MTV 패턴의 M

- [`views.py`](http://views.py/) : http요청을 처리하고 해당 요청에 대한 응답을 반환 ( url, model, template과 연계)
	- MTV 패턴의 V
- 템플릿은 기본적으로 제공되지않음, 개발자가 만들어야 함
- [`apps.py`](http://apps.py/) 앱의 정보가 작성된 곳
- [`test.py`](http://test.py/) 프로젝트 테스트 코드를 작성하는 곳

⇒ 수업과정에서 수정할 일 없음


# 요청과 응답


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/79c11ad7-949f-4fb0-99d5-bd0a2760d2c5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240313T162231Z&X-Amz-Expires=3600&X-Amz-Signature=9481410ef93590978a3c16dd98b8391d987b1b1f2b0d9d4c11749de6e15b4239&X-Amz-SignedHeaders=host&x-id=GetObject)


### 이 순서 = 데이터의 흐름


### 1. URLs


https:// 127.0.0.1:8000/index/ 로 요청왔을 때 views 모듈의 view 함수 index를 호출


```python
# urls.py
from django.contrib import admin
from django.urls import path

from articles import views          # 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('index/', 호출할 view 함수), 
    path('index/', views.index),     # 추가
]
```


### 2. View


특정 경로에 있는 template과 request 객체를 결합해 응답 객체를 반환하는 index view 함수 정의


```python
# views.py
from django.shortcuts import render

# 메인 페이지를 만드는 index라는 이름의 함수를 작성
def index(request): # 클라리언트가 보낸 객체 덩어리를 무조건 첫 인자로 받게 하는 '약속'
		# render 함수가 그렇게 만들어져 있다.
    # 랜더링 과정에 요청객체가 필요하다.
    # render(요청객체, 템플릿 경로)
    # 이 떄 템플릿 경로는 기본적으로 templates이후의 경로
    return render(request, 'articles/index.html')
```


모든 view 함수는 첫번째 인자로 request 요청 객체를 필수적으로 받음


request 이름 바꿔도 되지만(매개변수기 때문) 바꾸지 않음( 커뮤니티적 이유)


### 3. Template 

1. articles 앱 폴더 안에 templates 폴더 생성

	반드시 폴더 이름 templates여야 함

2. templates 폴더 안에 articles 폴더 생성
3. articles 폴더 안에 템플릿 파일 생성

### Django에서 template을 인식하는 경로 규칙


`app폴더 / templates /` 까지가 기본경로로 인식


⇒ view 함수에서 template 경로 작성 시 이 지점 이후의 경로를 작성해야 함


```python
def index(request):
	return render(request, 'articles/index.html')
```


### 데이터 흐름에 따른 코드 작성하기


URLs → View → Template 


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/15ad885e-8db8-4e35-a5ce-c83d14b64816/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240313T162231Z&X-Amz-Expires=3600&X-Amz-Signature=8a7891355244a05346d36808c2a602080d50d1e1bf9d7b04d7aa06e596e5e9f6&X-Amz-SignedHeaders=host&x-id=GetObject)


### MTV 디자인 패턴 정리

- Model
	- 데이터와 관련된 로직을 관리
	- 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
- Template
	- 레이아웃과 화면을 처리
	- 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
- View
	- Model & Template과 관련된 로직을 처리해서 응답을 반환
	- 클라이언트의 요청에 대해 처리를 분기하는 역할
- View 예시
	- 데이터가 필요하다면 model에 접근해서 데이터를 가져오고,
	- 가져온 데이터를 template로 보내 화면을 구성하고,
	- 구성된 화면을 응답으로 만들어 클라이언트에게 반환

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/ad7e4787-44e8-457f-9ce1-61b482ddca17/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240313T162231Z&X-Amz-Expires=3600&X-Amz-Signature=e13c4273cfe61d4fd0ca4e89d597ebb3308bfb4fc9a3bb91fbb239b0a321e42a&X-Amz-SignedHeaders=host&x-id=GetObject)


## render 함수 `render(request, tmeplate_name, context)`


주어진 탬플릿을 주어진 context 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse 응답 객체를 반환하는 함수

1. request : 응답을 생성하는 데 사용되는 요청 객체
2. template_name : 템플릿 이름의 경로
3. context : 템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)

# Django 규칙

1. [urls.py](http://urls.py/)에서 각 url 경로는 반드시 ‘/ ’ 로 끝남
2. [views.py](http://views.py/)에서 모든 view 함수는 첫 번째 인자로 요청 객체를 받음, 매개 변수 이름은 반드시 request로 지정
3. Django는 정해진 경로에 있는 tempate 파일만 읽어올 수 있음
	- app폴더/templates/이후

# 프레임워크의 규칙

- 프레임워크를 사용할 때는 일정한 규칙을 따라야 하며, 이는 저마다의 설계 철학이나 목표를 반영함
	- 일관성 유지, 보안 강화, 유지보수성 향상, 최적화 등과 같은 이유

> 프레임 워크는 개발자에게 도움을 주는 도구와 환경을 제공하기 위해 규칙을 정해 놓은 것이며 우리는 이를 잘 활용하여, 특정 기능을 구현하는 방법을 표준화하고 개발 프로세스를 단순화할 수 있도록 해야 함

