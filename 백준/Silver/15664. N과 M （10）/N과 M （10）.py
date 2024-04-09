import sys
input = sys.stdin.readline

# 15664 N과 M (10) 실버 2
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [False] * (n+1)
path = []
dicts = {}
def find(level):
    if len(path) == m:
        paths = path[:]
        paths.sort()
        dicts[tuple(paths)] = 1
    for i in range(n):
        if visited[i]: continue
        visited[i] = True
        path.append(arr[i])
        find(i)
        path.pop()
        visited[i] = False
find(0)
arrs = list(dicts.keys())
arrs.sort()
for i in arrs:
    print(*i)