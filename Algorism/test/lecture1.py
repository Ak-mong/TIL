# import sys; sys.stdin = open('algo1_sample_in.txt')
''' 내장함수 nim max sum abs 사용 X

'''
dij = [[0,1],[1,0],[0,-1],[-1,0]] #우 밑 왼 위
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # print("#",arr)
    max_v = 0
    for i in range(n):
        for j in range(n):
            sum_v = arr[i][j] # 쏜 곳의 점수로 초기화
            for k in range(4):
                for h in range(1,3): # 1, 2 칸 가는것
                    ni = i + dij[k][0]*h
                    nj = j + dij[k][1]*h
                    if 0<=ni<n and 0<=nj<n: # 벽체크
                        sum_v += arr[ni][nj]
            if max_v < sum_v:
                max_v = sum_v
    print(f'#{tc} {max_v}')
