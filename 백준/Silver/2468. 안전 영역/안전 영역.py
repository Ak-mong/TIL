# 2468 안전 영역
di = [0,0,1,-1] # 우 왼 하 상
dj = [1,-1,0,0]
from collections import deque

def dorwn_level(level):
    # 침수시키기
    for x in range(n):
        for y in range(n):
            if arr[x][y] <= level:
                drown[x][y] = 0

def bfs(r,c):
    deq = deque()
    deq.append((r,c))
    while deq:
        r,c = deq.popleft()
        visited[r][c] = 1
        for k in range(4):
            nr = r + di[k]
            nc = c + dj[k]
            if 0 <= nr < n and 0 <= nc < n: # 벽 체크
                if visited[nr][nc] == 0 and drown[nr][nc] == 1: # 갈수 있을 때
                    visited[nr][nc] = 1
                    deq.append((nr,nc))

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
max_v = 1
for p in range(1,101):
    drown = [[1] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    dorwn_level(p)
    for i in range(n):
        for j in range(n):
            if drown[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    if max_v < cnt:
        max_v = cnt
print(max_v)