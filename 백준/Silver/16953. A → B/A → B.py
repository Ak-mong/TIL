from collections import deque

def bfs(n,m):
    Q = deque()
    Q.append((n,1))
    while Q:
        v,cnt = Q.popleft()
        if v > m: continue
        if v==m:
            return cnt
        Q.append((v*2, cnt + 1))
        Q.append((v*10 + 1, cnt + 1))
    return -1

N,M = map(int,input().split())
path = []
print(bfs(N,M))