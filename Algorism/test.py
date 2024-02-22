import sys;sys.stdin =open('input.txt')

def maketree(node):
    global num
    # 왼 현 오
    if node <= n: # node가 n보다 작은 수 일때만
        maketree(node *2) #왼
        tree[node] = num # 현
        num += 1 # node에 들어갈 수가 1~6이기 때문
        maketree(node * 2 + 1)# 오



t = int(input())
for tc in range(1,t+1):
    n = int(input())
    # 루트 노드 : 1번 노드, 노드 != 값
    tree = [0] * (n+1) # 트리의 길이
    # print(tree)
    num = 1 # 완전트리임으로 사용
    maketree(1) # 시작 노드가 1번 노드
    print(f'#{tc} {tree[1]} {tree[n//2]}')


