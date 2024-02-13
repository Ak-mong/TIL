# Stack


물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조


스택에 저장된 자료는 `선형 구조` 를 갖는다

- 선형 구조 : 자료 간의 관계가 1대1의 관계를 갖는다.
- 비선형구조: 자료 간의 관계가 1대 N의 관계를 갖는다. (예: 트리)
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.

### 특성


마지막에 삽입한 자료를 가장 먼저 꺼낸다. 후입선출


예) 스택에 1,2,3 순으로 자료를 삽입 한 후 꺼내면 역순으로 즉 3,2,1순으로 꺼낼 수 있다.


### 스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산

- 자료구조 : 자료를 선형으로 저장할 저장소
	- 배열을 사용할 수 있다.
	- 저장소 자체를 스택이라 부르기도 한다.
	- 스택에서 마지막 삽입된 원소의 위치를 top이라고 부른다.
- 연산
	- 삽입: 저장소에 자료를 저장한다. 보통 push라고 부른다.
	- 삭제 : 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다. 보통 pop이라고 부른다.
	- 스택이 공백인지 아닌지를 확인하는 연산 `.isEmpty`
	- 스택의 top에 있는 item(원소)을 반환하는 연산 `.peek`

### 스택의 삽입/삭제 과정

- 빈 스택에 원소 A,B,C를 차례로 삽입 후 한번 삭제하는 연산과정

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/a56bf179-66f4-4b4a-a7df-fc0b125a59cc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240207T145629Z&X-Amz-Expires=3600&X-Amz-Signature=690a0445b18e809a69bc55d484304533a3383f27f4493a6f6bf65f8300aed20f&X-Amz-SignedHeaders=host&x-id=GetObject)

- top을 하나 증가시키고 top이 가르키는 자리에 a, b, c를 저장한다.
- 꺼낼 때는 top을 pop 하고 top을 하나 감소시킨다  `(순서 중요)`

### 스택의 push 알고리즘


append 메소드를 통해 리스트의 마지막에 데이터를 삽입


```python
def push(item): #파이썬 방법, list의 append 사용
	s.append(item)
```


### append 작동은 한 칸이 더해져 있는 배열을 `복사` 한 후  마지막에 넣는다.


⇒ 크기가 커질 수록 시간이 늘어나게 된다.


⇒ 스택으로 풀 수 있는지 확인하는 단계에서만 사용하는게 좋다


⇒ 크기가 고정된 배열과 pop만 이용하는 방법을 사용할 줄 알아야 된다.

- 스택의 구현

	```python
	def push(item, size): # 직접 구현하는 방법
		global top
		top += 1
		if top == size: # 디버깅용 코드
			print('overflow!'
		else:
			stack[top] = item

	size = 10
	stack = [0] * size
	top = -1

	push(10,size)
	top += 1 # push(20)
	stackptop] = 20
	```


### 스택의 pop 알고리즘


```python
def pop(): #list 의 pop을 쓰는 방법
	if len(s) == 0:
	 #underflow
		return 
	else:
		return s.pop()
```

- 스택의 구현

	```python
	def pop(): # pop 직접 구현
		global top
		if top == -1:
			print('underflow')
			return 0
		else:
			top -= 1
			return stack[top+1]

	print(pop())

	if top > -1: #pop() 보통 이렇게 짜는 편
		top -= 1
		print(stack[top+1])

	while top >=0: # while문 이용해서 할 수도 있다.
		top -= 1
	top = stack[top+1]
	```


	확인 → 꺼내기 → top 감소 : 대체로 확인하고 꺼내는 코드를 사용한다.


### 연습문제 1


	```python
	def push(n):
	    global top
	    top += 1
	    if top == size: # 디버깅용
	        print('Overflow!')
	    else:
	        stack[top] = n

	top = -1
	size = 10
	stack = [0] * size #최대 10개 push

	top += 1 #push(10)
	stack[top] = 10

	top += 1 #push(20)
	stack[top] = 20

	push(30)

	while top >= 0:
	    top -= 1
	    print(stack[top+1])
	```


### 고려사항

- 1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만 스택의 크기를 변경하기가 어렵다는 단점이 있다. (  메모리 낭비에도 불구하고 스택의 배열을 길게 만드는 이유, 파이썬은 나은 편)
- 이를 해결하기 위한 방법으로 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있다. 동적 연결리스트를 이용하여 구현하는 방법을 의미한다. 구현이 복잡하다는 단점이 있지만 메모리를 효율적으로 사용한다는 장점을 가진다. 스택의 동적 구현은 생략한다.

### 응용1 : 괄호 검사

- 괄호의 종류 : 대괄호,중괄호,소괄호
- 조건
	1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
	2. 같은 괄호에서 왼쪽괄호는 오른쪽 괄호보다 먼저 나와야 한다.
	3. 괄호 사이에는 포함관계만 존재한다.
	- 예 : a{b(c[d]e}f)
- 스택을 이용한 괄호 검사

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/51a30ef9-12cf-4070-8271-068b694a25c4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240207T145629Z&X-Amz-Expires=3600&X-Amz-Signature=5bd1e2edb93492ac30c4cccc53aa6a590f730aa362cb4a15aa0d367eab14b14e&X-Amz-SignedHeaders=host&x-id=GetObject)


`오류!` 2번째 : 닫는 괄호가 필요한데 스택이 비어있으면 오류


메모리에서는 ‘제거’라는 개념이 없음


 ⇒ 꺼내진 자리에 무언가 추가되면 그 자리를 덮어쓰게 됨


### 괄호를 조사하는 알고리즘 개요

- 문자열에 있는 괄호를 차례대로 조사하면서 왼쪽 괄호를 만나면 스택에 삽입하고, 오른쪽 괄호를 만나면 스택에서 top괄호를 삭제한 후 오른쪽 괄호와 짝이 맞는지를 검사
- 이 때, 스택이 비어 있으면 조건1 또는 조건 2에 위배되고 괄호의 짝이 맞지 않으면 조건 3에 위배된다.
- 마지막 괄호까지를 조사한 후에도 스택에 괄호가 남아 있으면 조건 1에 위배된다.

## 응용2 function call


### function call이란?

- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
	- 가장 마지막에 호출된 함수가 가장 먼저 실행이 완료하고 복귀하는 후입선출 구조이므로, 후입선출 구조의 스택을 이용하여 수행순서 관리
	- 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임(stack frame)에 저장하여 시스템 스택에 삽입
	- 함수의 실행이 끝나면 시스템 스택의 top원소(스택 프레임)를 삭제(pop)하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀
	- 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.

### 함수 호출과 복귀에 따른 전체 프로그램의 수행 순서


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/d947d817-ee9b-47f1-b9a3-f62c86b2c4e9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240207T145629Z&X-Amz-Expires=3600&X-Amz-Signature=d25f30048c4b02bc01207efe2a353ee481ce0e5d5845e3e7239137ecbd11a706&X-Amz-SignedHeaders=host&x-id=GetObject)


# 재귀 호출

- 필요한 함수가 자신과 같은 경우 자신을 다시 호출하는 구조
- 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성
- 구조적으로는 메모리 할당이 전부 다르기 때문(메모리 구분됨)에, 각 각 다른 함수를 호출하는 것과 동일하다. `(조심해야됨)`
	- f(1) 안에 f(1)이 호출되면 무한루프를 돌게 된다
- 재귀 호출의 예) factorial(`!`)

```python
main():
	f1()

def f1():
	f2()

def f2():
	f3()

def f3():
	~~~
	return ~
만
```


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/4e09ca64-3f0b-48bb-96e4-9f886e60ef4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240207T145629Z&X-Amz-Expires=3600&X-Amz-Signature=b649a5a654afededd881da1a9a45f970af703f261f03293f360b8789f7fd4033&X-Amz-SignedHeaders=host&x-id=GetObject)


# 파보나치 


일반적으로 재귀함수로 절대 안하는 편 (너무 오래걸려서)


0과 1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열


0,1,1,2,3,5,7,13 …


피보나치 수열의 i번 째 값을 계산하는 함수 F를 정의


F0 = 0, F1 = 1 


	⇒ Fi = Fi-1 + Fi-2 for i≥ 2


```python
def fibo(n):
	if n <2:
		return n
	else:
		return fibo(n-1) + fibo(n-2)
```


### 흐름도 : 복잡하다…


| 메모리              | 메모리              | 메모리              |       | 메모리                           |
| ---------------- | ---------------- | ---------------- | ----- | ----------------------------- |
| fibo(4)          | fibo(3)          | fibo(2)          | push→ | fibo(1)                       |
| fibo(3)+ fibo(2) | fibo(2)+ fibo(1) | fibo(1)+ fibo(0) | ←pop  | 1                             |
|                  |                  |                  | push→ | fibo(0)                       |
|                  |                  |                  | ←pop  | 0                             |
| n 을 만들고 4저장      | n 을 만들고 3저장      | n 을 만들고 2저장      |       | fibo(1) 과 fibo(0)
같은 메모리를 사용함 |


재귀함수 연습하는 방법


```python
def f(i,k): # i 현재위치, k 목효
    if i == k:
        return 
    else:
        print(arr[i])
        f(i+1,k)

arr = [10,20,30]
n = len(arr)
f(0 ,n) # 10 \n 20 \n 30

# 복사하는 작업
def f(i,k): # i 현재위치, k 목효
    if i == k:
        print(brr)
    else:
        brr[i] = arr[i]
        f(i+1,k) 

arr = [10,20,30]
n = len(arr)
brr = [0] * n
f(0 ,n) # [10,20,30]
```


피보나치 수를 구하는 함수를 재귀함수로 구현한 알고리즘은


` 엄청난 중복 호출이 존재한다. ` 라는 문제점이 있다.


### 피보나치 수열의 Call Tree (상태공간 트리)


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/813029fe-55f7-4efb-a653-80d7494157ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240207T145629Z&X-Amz-Expires=3600&X-Amz-Signature=5509f6b94cf790d0e141786927efa87df5022d4f1c585887295c3071f64e9631&X-Amz-SignedHeaders=host&x-id=GetObject)


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/be88415c-1be5-4443-9986-50bde35792ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240207T145629Z&X-Amz-Expires=3600&X-Amz-Signature=58c943b038835066c0d04448e4c41041dd664654c6f44bf67b734795d7ae0dc7&X-Amz-SignedHeaders=host&x-id=GetObject)


⇒ 메모이제이션 필요하다.


# 메모이제이션 memoization


메모`리`제이션이 아니라 메모이제이션이 맞다

- 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술이다.

	⇒ 동적 계획법의 핵심이 되는 기술이다.

- 메모이제이션은 글자 그대로 `메모리에 넣기(to put in memory)` 라는 의미
라틴어에서 파생
- 흔히 ‘기억하기’,’암기하기’ 라는 뜻의 memorization과 혼동

	but 정확한 단어는 memoization이다.


	동사형은 memoize이다.


```python
#memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다
#memo[0]을 0 으로 memo[1]는 1로 초기화 한다

def fibo1(n):
global memo
if n >= 2 and memo[n] == 0:
	memo[n] = fibo1(n-1) + fibo1(n-2)
return memo[n]

memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
```


### 기존 재귀함수와 메모이제이션 비교


```python
#메모리제이션이 아니라 메모이제이션이 맞다
def fibo(n):
    global cnt
    cnt += 1
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

cnt = 0
print(fibo(7),'횟수:', cnt)

# 메모이제이션
def fibo_memo(n):
    global cnt_memo
    cnt_memo += 1
    if n!=0 and memo[n] ==0:
        memo[n] = fibo_memo(n-1)+fibo_memo(n-2)
    return memo[n]

cnt_memo = 0
n = 7
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
print(fibo_memo(n),'횟수:',cnt_memo)
print(memo[n]) # 이렇게 해도 됨
print(memo) # 파보나치 리스트 호출
```


# 추가로 배운 것


### set, dict을 안 쓰고 중복 제거- 아스키 코드 사용해서


```python
asc = [0] * 128
alph = [] 

for i in range(len(str1)):
    asc[ord(str1[i])] = 1

for i in range(len(asc)):
    if asc[i]:
        alph.append(chr(i))
```


### 출력


```python
print(f'#{tc} {max_value}')
print("#{} {}".format(tc, max_value))
print('#%d %d' % (tc, max_value))

# 주의해야될 것
print('%f' % 12.5) # 12.500000
print('%.2f' % 12.5) # 12.50
print('%.0f' % 12.5) # 12, 반올림 해버린다. 옳지 않은 방법
print('%.0f' % 13.5) # 14, 반올림 해버린다. 옳지 않은 방법
print('%.0d' % int(12.5+0.5)) # 13 절사 진행하고 사용해버린다.
print('%.0d' % int(13.5+0.5)) # 14 절사 진행하고 사용해버린다.
```


### 스택 만들 시 주의해야 할것


```python
# 주의할 점, 스택의 크기를 아끼지 말자, 절대로 꽉차게 만들지 말자
# isEmpty는 체크하지만(pop할떄), isFull은 체크 안하게
# 리스트를 고정적으로 만들면 늘릴 방법이 없기 때문
def push(item):
    global top
    if top > maxsize -1:
        print('overflow') # 넘쳐버렸다, 실제로 여기로 들어오면 절대 안된다.
        return 0
    else:
        top += 1
        stack[top] = item

def pops():
    global top
    if top ==-1: # 항상 체크해줘야됨
        print('stack is empty')
        return
    else:
        """ 
        pop 이 이루어지고 나서 top을 하나 줄여야 되는데,
        return 다음에 top을 줄일수 없기 때문에 result에 값을 넣어놓고 result를 리턴함
        """
        result = stack[top]
        top -= 1
        return result


maxsize = 100
stack = [0] * maxsize
top = -1

push(1);push(2);push(3)
item = pops()
print(item)

while top != -1: # 굳이 pop한 것을 지울 필요는 없다.
    print(pops()) # 3 \n 2 \n 1

print(stack) # [1,2,3, ...]
```


간편 식


```python
maxsize = 100
stack = [0] * maxsize
top = -1
stack[top] = 1
#push
top += 1
stack[top] = 1
#push
top += 1
stack[top] = 2

#pop
if stack[top] != -1: #필수 요소
    item = stack[top]
    print(item)
    top -= 1
```


파이썬 방식


```python
# 파이썬 방식
stack = []

#push
stack.append(1)
stack.append(2)
stack.append(3)

# pop:
if stack: #stack이 안 비어 있다면
    print(stack.pop())
print(stack) # [] 이쪽은 진짜로 지워짐
```