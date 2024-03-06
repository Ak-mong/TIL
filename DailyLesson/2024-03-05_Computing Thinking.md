
# 프로그래밍과 논리/수학

1. 논리학
2. 알고리즘 성능 계산법 : 시간복잡도에 대해서 계산하는 방법

논리란?


이야기의 이치, 이야기의 올바른 연결


이치 : 과정의 순서가 올바르게 연결되었다.


### 논리학 :  형식이 중요하다.  ‘p 이면 q 이다’ 의 내용보단 형식이 중요하다.


ex) 농구


농구를 하는사람들은 키가 크다 = 근거


만약 농구를 하면 키가 커진다. False


명제란? p → q , True 또는 False로 판단할 수 있는 문장

1. 우체통은 빨갛다 명제 T F
2. 강사님은 잘생겼다 명제 T (’개인적인 생각’도 명제가 될 수 있음)
3. 주말에 시간있으세요? 명제 X → 의문문
4. 밖에 좀 나가서 운동해라 명제 X → 명령문

### 주장의 부정


주장을 제외한 모든 가능성을 포함하게 된다.


나는 강아지를 키운다 의 부정은 뭘까?


나는 고양이를 키운다. 나는 거북이를 키운다, 등등


# 오늘 강의에서 전제 2가지를 반드시 성립한다고 가정한다.

1. 배중률 : True / False 무조건 중간이 없는 것
	1. 무조건 False는 아니다 → True
2. 모순율 : True, False가 동시에 성립 하지 않는다.
	1. 원영이는 머리가 갈색이다.

# [참고]


‘이기다’의 부정 : 이기지 않다


‘이기다’의 반대 : 지다


‘나는 친구를 좋아한다’의 부정: 좋아하지 않는다.


‘나는 친구를 좋아한다’의 반대: 싫어한다.


민철이는 제주도에 간 적이 있다 → 없다


코코는 뉴욕에 살지 않는다.  → 산다


라면에는 마늘을 항상 넣어야 한다. → 하지 않다, or 가끔 넣는다 (모든 가능성을 포함한다.)


도현이는 지나치게 많이 먹는다. → 먹지 않다.


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/4ee8627c-d96b-4368-bbf1-5deecab1b65f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240305T120856Z&X-Amz-Expires=3600&X-Amz-Signature=fe6c1f70e20efa8457b2ddb1184a2def3df98e50daf03a6bd48a37804b5cd945&X-Amz-SignedHeaders=host&x-id=GetObject)


p → q 

1. 가정 명제가 거짓이라면 전체 명제식은 참이다
2. 대우 명제가 참이면 기존 명제도 참이다.

## 역, 이, 대우


주장 : 강아지는 포유류이다


역 ⇒명제 1 : 포유류는 강아지다 (앞, 뒤, 순서 변경)  q→ p


이 ⇒명제 2 : 이 동물이 강아지가 아니면, 포유류가 아니다.  ~p → ~q


대우 ⇒명제 3 : 이 동물이 포유류가 아니면, 강아지는 아니다.  ~q → ~p


### 대우가 참이면 주장도 참이다


논리 연습

1. 만약 0이 홀수라면, 미국에서 2080년 월드컵이 열린다.

	⇒ 가정이 거짓이다 → 전체 명제는 참

2. 만약 198938261837694839이 Prime Number라면 2는 짝수이다.
⇒ 대우를 이용해서 판단

	⇒ 2가 홀수면 == 거짓


	⇒ 가정이 거짓이다 → 전체 명제는 참


진리표


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/c901b240-ceef-42c0-b5e7-36fba5d61476/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240305T120856Z&X-Amz-Expires=3600&X-Amz-Signature=e67a9dec4831b5e13c6f706275b23cba05280403750e4e5696df3e853fc16891&X-Amz-SignedHeaders=host&x-id=GetObject)


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/0aff062b-ca53-4cbf-9e9e-05166d00e479/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240305T120856Z&X-Amz-Expires=3600&X-Amz-Signature=1001f1b39e32eaa5baf1f03877e56b664fbffd16a5adf7ca8fc18363cf6c4d33&X-Amz-SignedHeaders=host&x-id=GetObject)


# 기초 수식


### 연습 문제 : 다음 연산횟수식들을 O() notation 수준으로 풀어라


⇒ 시간복잡도 계산, 빅 오 표기법으로 풀어라


문제 1 : T(n) = T(n-1) + 1 , T(0) = 1


T(n-1)= T(n-2) + 1


T(n) = T(n-2) + 1 + 1 = T(n-2) + 2


T(n-2) = T(n-3) + 1


T(n) = T(n-3) + 3 = T(n-k) + k


= T(0) + n


= n + 1


재귀식을 빅 오 표기법으로 푼 방법


O(T(n)) = O(n)


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/8abfff3d-964a-4f32-9f21-8be219e81a0a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240305T120856Z&X-Amz-Expires=3600&X-Amz-Signature=f65f530030d721f894e26efb80635fbfc30c500ed540c17fa25eea46d1bd9635&X-Amz-SignedHeaders=host&x-id=GetObject)


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/902ea67b-167d-42e0-becb-4cd00fd26783/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240305T120856Z&X-Amz-Expires=3600&X-Amz-Signature=53eb44a7e79f9e3e3ce2704531059b6b68101e63db0a44e04b3a7de19f17bf23&X-Amz-SignedHeaders=host&x-id=GetObject)


O(T(n)) = O(nlogn)


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/c84ad466-d128-4d8d-a54e-30870cc9dd7c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240305T120856Z&X-Amz-Expires=3600&X-Amz-Signature=e4e5caabb9993e0c67c45dc35c8c3307d907b8d79b26e7c44f746152e4b72608&X-Amz-SignedHeaders=host&x-id=GetObject)


$∀$x 모든 x


$∃$x 어떤 x


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/2b512eae-5d63-45ba-ab6e-76beae0e9419/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240305T120858Z&X-Amz-Expires=3600&X-Amz-Signature=98cf298aacd4ba1af23cac2b30f2573e842e7aa228c59697fed9634955f582e9&X-Amz-SignedHeaders=host&x-id=GetObject)


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/cad8bbed-a5be-4e97-9d38-6dcd73eca4ea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240305T120859Z&X-Amz-Expires=3600&X-Amz-Signature=a7fd6874478f1ad78b244f049f47b42853b7f50639cd25a2de85911c8da48b69&X-Amz-SignedHeaders=host&x-id=GetObject)

