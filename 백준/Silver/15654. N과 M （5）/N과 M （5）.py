# 15654 n과m (5) 실버 3
def perm(level):
    if level == m:
        print(*path)
        return
    for i in range(n):
        if visited[i]:continue
        visited[i] = 1
        path.append(arr[i])
        perm(level+1)
        path.pop()
        visited[i] = 0
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
path = []
visited = [0] * n
perm(0)