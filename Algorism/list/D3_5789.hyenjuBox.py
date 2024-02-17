import sys;sys.stdin = open('txt/hyenjuBox')
T = int(input())
for tc in range(1,T+1):
    N, Q = map(int,input().split())
    arr = [0]*N
    for i in range(Q):
        L,R = map(int,input().split())
        for k in range(L-1,R):
            arr[k] = i+1
    print(f'#{tc}', *arr)