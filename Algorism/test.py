import sys;
sys.stdin =open('input.txt')
import time
# starttime = time.time()

# 2667 단지번호 붙이기
from collections import deque
def bfs(y,x):
    global cnt
    Q = deque()
    Q.append((y,x))
    visited[y][x] = 1
    while Q:
        y,x = Q.popleft()
        visited[y][x] = 1
        for direct in dij: # 4방향
            di = y + direct[0]
            dj = x + direct[1]
            if 0 <= di < n and 0 <= dj < n and arr[di][dj] and visited[di][dj] == 0:  # 벽체크 + 0이면 안간다
                arr[di][dj] += cnt
                visited[di][dj] = 1
                Q.append((di,dj))

def find_pos():
    flag = 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                r, c = i,j
                return (r,c-1)
    flag = 0
    return flag
n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
# cnt = [0] * n
dij = [[0,1],[1,0],[0,-1],[-1,0]] # 오 아 왼 위
visited = [[0] * n for _ in range(n)]
cnt = 1

while True:
    if find_pos():
        r, c = find_pos()
        bfs(r, c)
        cnt += 1
    else:
        break
# for l in arr:
#     print(l)

path = []
for k in range(2,cnt+1):
    cnt_num = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == k:
                cnt_num += 1
    if cnt_num != 0:
        path.append(cnt_num)
print(len(path))
for i in path:
    print(i)

'''
for i in range(n):
    for j in range(n):
        visited[i][j] = 1
        if arr[i][j]:
            for k in range(4):
                di = i + dij[k][0]
                dj = j + dij[k][1]
                if 0<= di < n and 0<= dj < n and arr[di][dj] and visited[di][dj] ==0: # 벽체크 + 0이면 안간다
                    visited[di][dj] = 1
                    arr[di][dj] += 1

'''