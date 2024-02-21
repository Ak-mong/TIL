import sys;sys.stdin = open('../txt/node_len.txt')
def solve(v):
    if v > n:
        return 0
    # 후위 순회
    if tree[v] == 0:
        tree[v] = solve(v*2) + solve(v*2+1)
    return tree[v]

t = int(input())
for tc in range(1,t+1):
    n,m,L = map(int,input().split())
    tree =[0] * (n+1)

    # 단말 노드 정보 저장
    for _ in range(m):
        node, value = map(int,input().split())
        tree[node] = value
    # 후위 순회 하면서 대해주면 된다.
    solve(1)
    print(f'#{tc} {tree[L]}')