
# 계산기

- 문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다.
- 문자열 수식 계산의 일반적 방법
	- step 1. 중위 표기법의 수식을 후위 표기법으로 변경한다. (스택 이용) ⇒ 계산기 1 (괄호가 제거됨)
		- 중위 표기법 (infix notation)

			연산자를 피연산자의 가운데 표기하는 방법 ex) $A+B$

		- 후위표기법 (postfix notation)

			연산자를 피연산자 뒤에 표기하는 방법 ex)  $AB+$

	- step 2. 후위 표기법의 수식을 스택을 이용하여 계산한다. ⇒ 계산기2

### Step1. 중위표기식의 후위표기식 변환 방법1

- 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현한다.
- 각 연산자를 그에 대응하는 오른쪽괄호의 뒤로 이동시킨다.
- 괄호를 제거한다.
- 예시

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/134240b0-fd3e-477e-a4ce-4e0c9de8083c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240213T130847Z&X-Amz-Expires=3600&X-Amz-Signature=403f437722e79525a802ab7b8e64b3810d18f8d5dc1ebfb285745630bbf5038a&X-Amz-SignedHeaders=host&x-id=GetObject)


### Step1. 중위 표기식의 후위 표기식 변환 알고리즘( 스택 이용)2


토큰 : 더 이상 다를 수 없는 단위

1. 입력 받은 중위 표기식에서 토큰을 읽는다.
2. 토큰이 피연산자이면 토큰을 출력한다.
3. 토큰이 연산자(괄호포함)일 때,

	이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고,


	그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop 한 후 토큰의 연산자를 push한다.


	만약 top에 연산자가 없으면 push한다.

4. 토큰이 오른쪽 괄호 `‘)’`이면 스택 top에 왼쪽 괄호 `‘(’`가 올 때까지 스택에 pop 연산을 수행하고 pop 한 연산자를 출력한다. `왼쪽 괄호`를 만나면 pop만 하고 출력하지는 않는다.
`( )` 을 제거한다는 말
5. 중위 표기식에 더 읽을 것이 없다면 중지, 더 읽을 것이 있다면 1부터 다시 반복
6. 스택에 남아 있는 연산자를 모두 pop하여 출력한다.

### 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮다.
⇒ `스택 밖에서는(ICP)에서는 왕, 스택 안에서는(ISP)에서는 노비`


우선 중위 표기법에서 후위 표기법으로의 변환한다.


중위 표기법으로 표현된 수식 예 :  $(6 + 5 * (2-8) / 2)$


## Step2. 후위 표기법의 수식을 스택을 이용하여 계산

1. 피연산자를 만나면 스택에 push 한다.
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push 한다.
3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력한다.

# 백트래킹

- 백트래킹(Backtracking) 기법은 해를 찾는 도중에 `막히면` (즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법이다.
- 백트래킹 기법은 `최적화`(optimization)문제와 `결정`(decision, 0 or 1 )문제를 해결할 수 있다.
- 결정 문제: 
문제의 조건을 만족하는 해가 존재하는지의 여부를 ‘yes’또는 ‘no’가 답하는 문제
	- 미로 찾기
	- n-Queen 문제
	- Map coloring
	- 부분 집합의 합(Subset Sum) 문제 등

## 백 트래킹과 깊이우선탐색(DFS)과의 차이

- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않음으로써 시도의 횟수를 줄임(Prunning 가지치기)
- DFS가 모든경우를 추적함에 비해 백트래킹은 불필요한 경로를 조기에 차단
- DFS을 가하기에는 경우의 수가 너무나 많음. 즉 $N!$ 가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 `처리 불가능`한 문제
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만, 이 역시 최악의 경우에는 지수함수 시간(Exponential Time)을 요하므로 `처리 불가능`

## 백트래킹 : 모든 후보를 검사? No


### 백트래킹 기법

- 어떤 노드의 `유망성`을 점검한 후에 유망(`promising`)하지 않다고 결정되면 그 Node의 부모로 되돌아간(backtracking) 다음 자식 노드로 감
- 어떤 노드를 방문하였을 때 
그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며,
반대로 해답의 가능성이 있으면 유망하다고 한다.
- 가지치기(pruning) : 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않는다.

### 백트래킹 사용한 알고리즘의 절차

1. 상태 공간 트리의 DFS을 실시한다.

	상태공간트리(= 정리해놓고 보니 이러한 모양이 되더라)

2. 각 노드가 유망한지를 점검한다.
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.

### 일반 백트래킹 알고리즘


```python
def checknode(v) : #node
	if promising(v):
		if there is a solution at v:
			write the solution
		else:
			for u in each child of v:
				checknode(u)
```


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/1f08e124-58d0-491f-9f76-b485d13f5aba/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240213T130847Z&X-Amz-Expires=3600&X-Amz-Signature=f04fc2b47a88d1507e778b8db0ac79067e289f75f632ec78b09909b35957db35&X-Amz-SignedHeaders=host&x-id=GetObject)


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/437a1382-d126-41f0-987b-3fce346d0f48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240213T130849Z&X-Amz-Expires=3600&X-Amz-Signature=5b8f0d0a0705b5281195c495c5fb652d4858539b523b9b7d0b19bc893cc01782&X-Amz-SignedHeaders=host&x-id=GetObject)


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/00bf6eaa-f13e-4c60-8602-7b077c22e3d1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240213T130850Z&X-Amz-Expires=3600&X-Amz-Signature=19c6b88910147454223c217a18f8aeaec75b8cb50d0c45c293d07cf3024908f2&X-Amz-SignedHeaders=host&x-id=GetObject)


상태 공간 트리


### 깊이 우선 검색 vs 백트래킹


155 노드            vs         27 노드


# 부분 집합


### 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합을 `powerset`이라고 하며 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 $2^n$개 이다.


백트래킹 기법으로 `powerset`을 만들어 보자.

- 앞에서 설명한 일반적인 백트래킹 접근 방법을 이용한다.
- n개의 원소가 들어있는 집합의 $2^n$개의 부분집합을 만들 때는, true 또는 false값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용
- 여기서 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값 이다.

각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 방법 `원소 개수 = for문의 개수`


```python
bit = [0,0,0,0]
for i in range(2):
	bit[0] = i # 0번째 원소
	for j in range(2):
		bit[1] = j # 1번째 원소
		for k in range(2):
			bit[2] = k # 2번째 원소
			for h in range(2):
				bit[3] = h # 3번째 원소
				print(bit) # 생성된 부분집합 출력
```


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/79ce2aad-a0f9-41af-8554-dca38e8460b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240213T130847Z&X-Amz-Expires=3600&X-Amz-Signature=a31b844871ce80ce9cabcf994c98163fdf1839bd15b14c4f864a76e25e26efa4&X-Amz-SignedHeaders=host&x-id=GetObject)


### powerset을 구하는 백트래킹 알고리즘


```python
def backtrack(a,k, input):
	global MAXCANDIDATES
	c = [0] * MAXCANDIDATES
	if k == input:
		process_solution(a,k) # 답이면 원하는 작업을 한다
	else:
		k += 1
		ncandidates = construct_candidates(a,k, input, c)
		for i in range(ncandidates):
			a[k] =c[i]
			backtrack(a,k,input)

def construct_candidates(a,k, input,c):
	c[0] = True
	c[1] = False
	return 2

MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
backtrack(a,0,3)
```


### 응용 코드


```python
def f(i,k):
    if i==k:
        for j in range(k):
            if bit[j]:
                print(arr[j],end=' ')
        print()
    else:
        # for j in range(2): #밑과 같은 코드
        #     bit[i] = j
        #     f(i+1, k)
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)
N = 4
arr = [1,2,3,4]
bit = [0] * N # bit[i] : arr[i] 가 부분집합에 포함되었는지 나타내는 배열
f(0,N) # bit[i]에 1또는 0을 채우고, N개의 원소가 결정되면 부분집합을 출력
```


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/526b4b2f-52a7-472d-89c7-355bd22a00f0/5e8c400b-e907-4e93-941f-f0a0f857bde7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240213T130847Z&X-Amz-Expires=3600&X-Amz-Signature=6429af9a3d4f28480a930339450aefdea9a3c70cda2f085b639863543cc93263&X-Amz-SignedHeaders=host&x-id=GetObject)

