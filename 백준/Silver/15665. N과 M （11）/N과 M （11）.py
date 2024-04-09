import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 15665 n과 M (11) 실버2
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [False] * (n+1)
path = []
dicts = {}
def find(level):
    # if visited[level]: return
    if len(path) == m:
        paths = tuple(path)
        dicts[paths] = 1
        return
    for i in range(n):
        # visited[i] = True
        path.append(arr[i])
        find(i)
        path.pop()
        # visited[i] = False

find(0)
for p in dicts.keys():
    print(*p)