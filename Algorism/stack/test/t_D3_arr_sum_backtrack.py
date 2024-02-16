import sys;sys.stdin = open('../txt/arr_sum.txt')

def perm(n,k,cursum):
    global ans,cnt
    cnt += 1
    # 가지치기 #####################
    if ans < cursum: return
    ###############################
    if n ==k:
        if ans > cursum:
            ans = cursum
    else:
        for i in range(k,n):
            A[k], A[i] = A[i], A[k]
            perm(n,k+1, cursum + arr[k][A[k]])
            A[k], A[i] = A[i], A[k]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    A = list(range(N))
    ans = 0xffffffff
    cnt = 0
    perm(N,0,0)
    print(f'#{tc} {ans}')
    print(cnt)