import sys
from collections import deque
input = sys.stdin.readline

# 24445 너비 우선 탐색 2 실버2

n,m,r = map(int,input().split())
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adjl[a].append(b)
    adjl[b].append(a)
visited = [0] * (n+1)
def bfs(start):
    cnt = 1
    deq = deque()
    deq.append(start)
    while deq:
        value = deq.popleft()
        if visited[value]: continue
        adjl[value].sort(reverse=True)
        visited[value] = cnt
        cnt += 1
        for i in adjl[value]:
            deq.append(i)
bfs(r)
# print(adjl)
for p in range(1,n+1):
    print(visited[p])