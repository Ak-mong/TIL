import sys; sys.stdin = open('../txt/graph_route.txt')

def dfs(v):
    global flag
    # 방문체크
    visited[v] = 1
    if v == end: # flag 사용한 하나의 방법
        flag = 1
        return 
    # v에 인접한 정점(w)중에 미방문 정점을 재귀호출
    for w in range(1,V+1):
        if adj[v][w] and not visited[w]:
            dfs(w)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        n1, n2 = map(int,input().split())
        adj[n1][n2] = 1 # 방향성 있음
    start, end = map(int,input().split())
    flag = 0
    dfs(start)
    print(f'#{tc} {visited[end]}')
    print(f'#{tc} {flag}') #flag 사용했을 때 출력 방법