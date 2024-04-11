import sys
from collections import deque
input = sys.stdin.readline

# 31575 도시와 비트코인 실버 3
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
dij = [[0,1],[1,0]]
def bfs():
    deq = deque()
    deq.append((0,0))
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True
    while deq:
        global result
        r,c = deq.popleft()
        if r == m-1 and c == n-1:
            return True
        for dr, dc in dij:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and arr[nr][nc] == 1:
                deq.append((nr,nc))
                visited[nr][nc] = True
    return False
if bfs():
    print('Yes')
else:
    print('No')