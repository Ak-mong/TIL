import sys
from collections import deque
input = sys.stdin.readline

# 24447 너비 우선 탐색 4 실버2
n,m,r = map(int,input().split())
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adjl[a].append(b)
    adjl[b].append(a)
deq = deque()
deq.append(r)
visited = [0] * (n+1)
depth = [0] * (n+1)
cnt = 1
visited[r] = cnt
while deq:
    # cnt += 1
    value = deq.popleft()
    adjl[value].sort()
    for i in adjl[value]:
        if visited[i]: continue
        cnt += 1
        visited[i] =  cnt
        depth[i] = depth[value] + 1
        deq.append(i)
sum_v = 0
for x in range(1,n+1):
    sum_v += visited[x] * depth[x]
print(sum_v)