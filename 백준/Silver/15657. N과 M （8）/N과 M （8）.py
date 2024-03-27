# 15657 N 과 M (8)
# 중복 순열, 오름차순
def perm(x):
    if len(path) == m:
        print(*path)
        return
    for i in range(x,n):
        path.append(arr[i])
        perm(i)
        path.pop()

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
path = []
perm(0)