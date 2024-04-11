import sys
from collections import deque
input = sys.stdin.readline
# 24446 너비 우선 탐색 3 실버2
n,m,r = map(int,input().split())
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adjl[a].append(b)
    adjl[b].append(a)
visited = [False] * (n+1)
depth = [0] * (n+1)
deq = deque()
deq.append(r)
cnt = 1
while deq:
    value = deq.popleft()
    if visited[value]: continue
    visited[value] = True
    # adjl[value].sort()
    for i in adjl[value]:
        if visited[i] or depth[i]: continue
        depth[i] = depth[value] + 1
        deq.append(i)
# print(adjl)
# print(visited[1:])
for p in range(1,n+1):
    if p != r and depth[p] == 0:
        print(-1)
    else:
        print(depth[p])