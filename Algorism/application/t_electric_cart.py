import sys;sys.stdin = open('txt/electric_cart.txt')

def perm(level, cursum):
    global min_v
    if min_v < cursum: return
    if level == n:
        cursum += arr[path[n - 1]][path[0]]
        if min_v > cursum: min_v = cursum
        return
    for i in range(1,n):
        if used[i]: continue
        used[i] = 1
        path.append(i)
        perm(level+1 , cursum + arr[path[level-1]][path[level]])
        path.pop()
        used[i] = 0

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    path = [0]
    used = [0] * n
    used[0] = 1
    min_v = 987654321
    perm(1,0)
    print(f'#{tc} {min_v}')
