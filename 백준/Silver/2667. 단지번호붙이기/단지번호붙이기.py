# 2667 단지번호 붙이기
from collections import deque
def bfs(y,x):
    global cnt
    num = 0
    if arr[y][x] ==0: return
    if visited[y][x]: return
    Q = deque()
    Q.append((y,x))
    while Q:
        y,x = Q.popleft()
        num += 1
        visited[y][x] = 1
        if arr[y][x] == 1: arr[y][x] += cnt
        for direct in dij: # 4방향
            di = y + direct[0]
            dj = x + direct[1]
            if 0 <= di < n and 0 <= dj < n: # 벽 체크
                if visited[di][dj] == 0: # 안 가본곳이라면
                    if arr[di][dj] ==0:
                        visited[di][dj] = 1
                    else:
                        arr[di][dj] += cnt
                        visited[di][dj] = 1
                        Q.append((di,dj))
    cnt += 1
    path.append(num)

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
dij = [[0,1],[1,0],[0,-1],[-1,0]] # 오 아 왼 위
visited = [[0] * n for _ in range(n)]
path = []
cnt = 0
# 시작 지점
for i in range(n):
    for j in range(n):
        bfs(i, j)
path.sort()
print(cnt)
for i in path:
    print(i)