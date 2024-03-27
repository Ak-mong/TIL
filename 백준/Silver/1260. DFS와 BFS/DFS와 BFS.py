# 1260 DFS 와 BFS 실버2
from collections import deque
def dfs(v):
    visited_d[v] = 1
    path.append(v)
    for i in range(1,n+1):
        if not visited_d[i] and adjl[v][i]:
            dfs(i)
def bfs(v):
    visited_b = [0] * (n + 1)
    deq = deque()
    deq.append(v)
    visited_b[v] = 1
    path_b = []
    while deq:
        value = deq.popleft()
        path_b.append(value)
        for i in range(1,n+1):
            if not visited_b[i] and adjl[value][i]:
                visited_b[i] = 1
                deq.append(i)
    return path_b
n, m, v = map(int,input().split())
adjl = [[False] *(n+1) for _ in range(n+1)]
for i in range(m):
    s,e = map(int,input().split())
    adjl[s][e] = True
    adjl[e][s] = True
path = []
visited_d = [0] * (n+1)
dfs(v)
print(*path)
print(*bfs(v))