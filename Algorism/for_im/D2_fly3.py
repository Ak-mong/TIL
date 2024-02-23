import sys;

sys.stdin = open('D2_fly3.txt')

'''
NxN 에 m 만큼의 길이로 
'''
drc_plus = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 위~왼위까지
drc_x = [(-1, 1), (1, 1), (1, -1), (-1, -1)]  # 위~왼위까지
# print(drc[0][1])
t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_fly = 0
    for i in range(n):
        for j in range(n):
            kill_fly_p = 0  # 파리 초기화
            kill_fly_x = 0  # 파리 초기화
            # 십자 4방향 탐색
            for k in range(4):
                # p 방향의 m거리만큼 탐색
                for p in range(1, m):  # 1 2
                    ni, nj = i + drc_plus[k][0] * p, j + drc_plus[k][1] * p
                    if 0 <= ni < n and 0 <= nj < n:  # 벽 체크
                        kill_fly_p += arr[ni][nj]
                for x in range(1, m):
                    ni, nj = i + drc_x[k][0] * x, j + drc_x[k][1] * x
                    if 0 <= ni < n and 0 <= nj < n:  # 벽 체크
                        kill_fly_x += arr[ni][nj]
            kill_fly_p += arr[i][j]
            kill_fly_x += arr[i][j]
            if max_fly < kill_fly_p:  # 십자
                max_fly = kill_fly_p
                # print('p',i,j,max_fly)
            if max_fly < kill_fly_x:  # x자
                max_fly = kill_fly_x
                # print('x',i,j,max_fly)

    print(f'#{tc} {max_fly}')
