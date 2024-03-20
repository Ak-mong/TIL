import sys;sys.stdin=open('min_product.txt')

def perm(level,cursum):
    global min_v,cnt
    if cursum > min_v: return
    cnt += 1
    if level == n:
        # min_v = min(min_v,sum(path))
        min_v = min(min_v,cursum)
        return
    for i in range(n):
        if used[i]: continue
        used[i] = True
        # path.append(arr[level][i])
        perm(level+1,cursum + arr[level][i])
        # path.pop()
        used[i] = False

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    path = []
    used = [False] * n
    min_v = 9999999999999999
    cnt = 0
    perm(0,0)
    print(min_v, cnt)
