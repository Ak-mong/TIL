import sys;sys.stdin = open('../txt/arr_sum.txt')

def perm(n,k):
    global ans, cnt
    cnt += 1
    if n ==k:
        sum_v = 0
        for i in range(n):
            sum_v += arr[i][A[i]]
        if ans > sum_v:
            ans = sum_v
    else:
        for i in range(k,n):
            A[k], A[i] = A[i], A[k]
            perm(n,k+1)
            A[k], A[i] = A[i], A[k]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    A = list(range(N))
    ans = 0xffffffff
    cnt = 0
    perm(N,0)
    print(f'#{tc} {ans}')
    print(cnt)