"""
V, E : V 1~V 까지 V개의 정점. E개의 간선
E개의 간선정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def bfs(s,N): # s : 시작정점 s, 노드 개수 N
    q = []                      # 큐
    visited = [0] * (N+1)       # visited
    q.append(s)                 # 시작점 인큐
    visited[s] = 1              # 시작점 방문표시
    while q:                    # 큐가 비워질때까지... (남은 정점이 있으면)
        t = q.pop(0)
        # t에서 할 일일
        print(t, end=' ')       # 1 2 3 4 5 7 6
        for i in adjl[t]:       # t에 인접인 정점을 꺼내서
            if visited[i] ==0:  # 방문하지 않았네?
                q.append(i)     # 인큐
                visited[i] = 1 + visited[t] # 방문표시
    print(visited)              # [0, 1, 2, 2, 3, 3, 4, 3]
V, E = 7, 8
arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# 인접리스트
adjl = [[] for _ in range(V+1)] # [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)         # 무방향 그래프

bfs(1, V)
bfs(4, V)                       #4 2 6 1 5 7 3 [0, 3, 2, 4, 1, 3, 2, 3]