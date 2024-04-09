import sys
from collections import deque
input = sys.stdin.readline

# 7576 토마토 골드 5
di = [0,0,-1,1]
dj = [1,-1,0,0]
def bfs():
    deq = deque()
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                deq.append((i,j,1))
    while deq:
        r,c,day = deq.popleft()
        for k in range(4):
            nr = r + di[k]
            nc = c + dj[k]
            if 0<=nr<n and 0<=nc < m:
                if tomato[nr][nc] == 0:
                    tomato[nr][nc] = day
                    deq.append((nr,nc,day+1))

m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]
bfs()
def find():
    max_value = 0
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                return -1
            else:
                if max_value < tomato[i][j]:
                    max_value = tomato[i][j]

    if max_value == 1:
        return 0
    else:
        return max_value
print(find())