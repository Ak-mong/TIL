import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 24480 알고리즘 수업 - 깊이 우선 탐색 2
n,m, r = map(int,input().split())
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    adjl[s].append(e)
    adjl[e].append(s)
visited = [0] * (n+1)
cnt = 1
def dfs(level):
    global cnt
    if visited[level]: return
    visited[level] = cnt
    adjl[level].sort(reverse=True)
    for i in adjl[level]:
        if visited[i]:continue
        cnt += 1
        dfs(i)

dfs(r)
for p in range(1,n+1):
    print(visited[p])