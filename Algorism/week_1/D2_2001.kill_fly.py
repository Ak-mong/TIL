import sys; sys.stdin = open('txt/kill_fly.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)
    max_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            max_v = 0
            for m in range(M):
                for n in range(M):
                    max_v += arr[i+m][j+n]
            max_list.append(max_v)
    for k in max_list:
        if max_v < k:
            max_v = k
    print(f'#{tc} {max_v}')

