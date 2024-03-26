# 15656 n과 m (7)
def perm(level):
    if len(path) == m:
        print(*path)
        return
    for i in range(n):
        path.append(arr[i])
        perm(i+1)
        path.pop()

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

path = []
visited = [0] * n
perm(0)