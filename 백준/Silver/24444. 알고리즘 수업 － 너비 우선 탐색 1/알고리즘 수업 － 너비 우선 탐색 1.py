import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 24444 너비 우선 탐색 1 실버 2
n,m,r = map(int,input().split())
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    adjl[s].append(e)
    adjl[e].append(s)
visited = [0] * (n + 1)
def bfs(level):
    cnt = 1
    deq = deque()
    deq.append(level)
    while deq:
        value = deq.popleft()
        if visited[value]: continue
        visited[value] = cnt
        cnt += 1
        adjl[value].sort()
        for i in adjl[value]:
            if visited[i]: continue
            deq.append(i)
bfs(r)
for p in range(1,n+1):
    print(visited[p])