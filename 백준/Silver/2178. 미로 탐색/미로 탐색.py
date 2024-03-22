# 2178 미로 탐색 실1
from collections import deque
di = [1,-1,0,0] # 상하좌우
dj = [0,0,-1,1]
n, m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
path = []
cnt = 0

que = deque()
que.append((0,0))
visited[0][0] = 1  # 붕문처리
while que:
    y,x = que.popleft()
    for k in range(4):
        ni = y + di[k]
        nj = x + dj[k]
        if 0<= ni < n and 0<= nj < m: # 벽체크
            if arr[ni][nj] ==1: # 1일때만 간다
                if visited[ni][nj]: continue
                visited[ni][nj] = visited[y][x] +1
                # arr[ni][nj] = 3
                path.append((ni, nj))
                cnt += 1
                que.append((ni,nj))

print(visited[n-1][m-1])