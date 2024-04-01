# 1012 유기농 배추 실버 2
from collections import deque

di = [1,-1,0,0]
dj = [0,0,-1,1]

t = int(input())
for _ in range(t):
    m, n, k = map(int,input().split())
    arr = [[0]*(m+1) for _ in range(n+1)]
    visited = [[0]*(m+1) for _ in range(n+1)]
    cnt = 0
    for _ in range(k):
        c,r = map(int,input().split())
        arr[r][c] = 1
    # print('#',t)
    # for p in arr:
    #     print(p)
    for i in range(n):
        for j in range(m):
            if arr[i][j] and visited[i][j] == 0:
                visited[i][j] = 1 # 방문 체크
                cnt += 1
                que = deque()
                que.append((i,j))
                while que:
                    r,c = que.popleft()
                    for q in range(4):
                        nr = r + di[q]
                        nc = c + dj[q]
                        if 0<=nr<n and 0 <= nc < m and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            que.append((nr,nc))
    print(cnt)