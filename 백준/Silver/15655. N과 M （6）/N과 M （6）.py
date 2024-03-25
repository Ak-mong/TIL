# 15655 n과m (6) 실버 3
def perm(level):
    if len(path) == m:
        print(*path)
        return
    for i in range(level,n):
        if visited[i]: continue
        visited[i] = 1
        path.append(arr[i])
        perm(i+1)
        path.pop()
        visited[i] =0

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
path = []
visited = [0] * (n+1)
perm(0)