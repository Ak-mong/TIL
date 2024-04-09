import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 깊이 우선 탐색 3 실버 2
n,m,r = map(int,input().split())
adjl = [[] for _ in range(n+1)]
visited = [False] * (n+1)
depth = [0] * (n+1)
for _ in range(m):
    s,e = map(int,input().split())
    adjl[s].append(e)
    adjl[e].append(s)
    
def dfs(level):
    if visited[level]: return
    visited[level] = True
    adjl[level].sort()
    for i in adjl[level]:
        if visited[i]: continue
        depth[i] = depth[level] + 1
        dfs(i)
dfs(r)
# print(adjl)
# print(visited)
# print(depth)
for p in range(1,n+1):
    if visited[p]:
        print(depth[p])
    else:
        print(-1)