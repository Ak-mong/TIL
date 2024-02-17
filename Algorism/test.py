import sys; sys.stdin = open('input.txt')
import time
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) # 5 2
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)
    dij = [[0,1],[1,0],[0,0],[1,1]]
    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_v = 0 # 한 좌표마다 초기화
            for x in range(M): # 0 1
                for y in range(M): # 0 1
                    sum_v += arr[i+x][j+y]
            if max_v < sum_v:  # 최대 값 비교
                max_v = sum_v
    print(f'#{tc} {max_v}')
