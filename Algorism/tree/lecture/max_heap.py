# 최대 힙
def enque(n):
    global last
    last += 1 # 마지막 노드 추가(완전이진트리 유지를 위함)
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last # 부모 > 자식 비교를 위해
    p = c//2 # 부모번호 계싼
    while p >= 1 and h[p] < h[c]: # 부모가 있는데 부모가 자식보다 잘다면?
        h[p], h[c] = h[c],  h[p] # 교환
        c = p
        p = c//2
def deque():
    global last
    tmp = h[1] # 루트의 키 값 보관
    h[1] = h[last]
    last -= 1 # 루트 노드 삭제
    p = 1 # 새로 옮긴 루트
    c = p * 2
    while c<= last: # 자식이 있으면
        if c+1 <= last and\
            h[c] < h[c+1]: # 오른쪽 자식이 있고 더 크다면?
            c += 1 # 오른쪽 자식은 부모 * 2 + 1 이기 때문
        if h[p] < h[c]: # 부모가 자식보다 작다면
            h[p], h[c] = h[c], h[p]
            p = c # 자식을 새로운 부모로 해서
            c = p * 2 #
        else:
            break
    return tmp

N = 10 # 필요한 노드 수
h = [0] * (N+1) # 비어있는 힙
last = 0 # 힙의 마지막 노드 번호
for i in [2,5,3,6,4]:
    enque(i)
print('전',h)
while(last>0):
    print(deque())
print('후',h)