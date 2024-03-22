import sys;
sys.stdin =open('input.txt')
import time
# starttime = time.time()
# from collections import deque
# def bfs(a): # a를 b로 바꿔야된다
#     que = deque()
#     que.append(a)
#
#     while que:
#
# n,m = map(int,input().split())
#
# bfs(n)
import time
starttime = time.time()
from collections import deque
def bfs(n,m):
    Q = deque()
    Q.append(n)
    visited[n] = 1
    while Q:
        v = Q.popleft()
        if v > m: continue
        if v==m:
            return visited[m]
        for w in [v*2,int(str(v)+'1')]:
            if 0< w <= m:# 백만 이하의 자연수
                if visited[w] ==0:
                    visited[w] = visited[v] + 1
                    Q.append(w)
    return -1


N,M = map(int,input().split())
visited = [0] * (M + 1)
print(bfs(N,M))
print(time.time()-starttime)