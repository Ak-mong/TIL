# 4964 섬의 개수 실버 2
import sys
from collections import deque
input = sys.stdin.readline

di = [0,0,1,-1,-1,1,-1,1]
dj = [1,-1,0,0,1,1,-1,-1]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    maps = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0] * (w+1) for _ in range(h)]
    cnt = 0
    # for p in maps:
    #     print(p)
    def bfs():
        global cnt
        for i in range(h):
            for j in range(w):
                if maps[i][j] == 1 and not visited[i][j]:
                    deq = deque()
                    deq.append((i,j))
                    visited[i][j] = 1
                    while deq:
                        r,c = deq.popleft()
                        for k in range(8):
                            nr = r + di[k]
                            nc = c + dj[k]
                            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and maps[nr][nc] == 1:
                                visited[nr][nc] = 1
                                deq.append((nr,nc))
                    cnt += 1
    bfs()
    print(cnt)