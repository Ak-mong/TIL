import sys

# 7569 토마토 골드 5
from collections import deque
dy = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
def bfs():
    global flag
    deq = deque()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if arr[k][i][j] == 1 and visited[k][i][j] == -1: # 익은 토마토 찾기
                    deq.append((k,i,j))
                    visited[k][i][j] = 0
    while deq:
        z,y,x = deq.popleft() # 높이, 세로, 가로
        for p in range(6):
            ny = y + dy[p]
            nx = x + dx[p]
            nz = z + dz[p]
            if 0<= ny < n and 0 <= nx < m and 0 <= nz < h: # 4방향 체크
                if visited[nz][ny][nx] == -1 and arr[nz][ny][nx] == 0:
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    deq.append((nz,ny,nx))

def find():
    global flag,max_v
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if arr[k][i][j] == 0 and visited[k][i][j] == -1:
                    flag = 0
                    return
                if max_v < visited[k][i][j]:
                    max_v = visited[k][i][j]
m, n, h = map(int,input().split())
arr = []
for i in range(h):
    arr.append([list(map(int,input().split())) for _ in range(n)])
flag = 1
max_v = 0
visited = [[[-1] * (m) for _ in range(n)] for _ in range(h)]
bfs()
find()
if flag:
    if max_v ==0:
        print(0)
    else:
        print(max_v)
else:
    print(-1)
