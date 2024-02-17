import sys; sys.stdin = open('txt/oselo.txt')
from collections import deque
# 8방향 탐색이 필요하다
dr = [0,1,1, 1, 0,-1,-1,-1]
dc = [1,1,0,-1,-1,-1, 0, 1]
def oselo(arr):
    while dol_arr: # 덱이 존재하는  동안
        r, c, color = dol_arr.popleft() #하나씩 뽑아버린다.
        arr[r-1][c-1] = color # 해당 좌표에 색을 칠한다.
        for k in range(8):
            nr = r-1 + dr[k]
            nc = c-1 + dc[k]
            change = [[nr,nc]] # 바로 옆 돌 저장

            # 벽체크 와 해당 방향으로 빈칸이 아닌 다른 색의 돌이 나올 때 마다 change에 저장시킨다.
            while 0<= nr<N and 0<= nc<N and arr[nr][nc] != 0 and arr[nr][nc] != color:
                nr += dr[k]
                nc += dc[k]
                change.append([nr,nc])
            # print(change)
            # change에 있는 좌표들을 벽체크하고 전부 다 바꿔준다.
            # change에 인접좌표 넣으면서 초기화 했기 때문에 무조건 1개 들어있다.
            # nr,nc 좌표에 돌이 없을 수도 있다. 검 흰흰 0
            if len(change) > 1 and 0<= nr<N and 0<= nc<N and arr[nr][nc] != 0:
                for x,y in change:
                    arr[x][y] = color # 해당 좌표의 색을 같은 색으로 맞춘다.
    # print(arr)
    # 갯수 세기
    b_cnt = 0
    w_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                b_cnt += 1
            elif arr[i][j] == 2:
                w_cnt += 1
    return b_cnt,w_cnt
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) # N: 보드의 한 변 길이, M = 돌을 놓는 횟수
    arr = [[0] * (N) for _ in range(N)]
    arr[N//2-1][N//2] = 1 #흑
    arr[N//2-1][N//2-1] = 2 # 백
    arr[N//2][N//2-1] = 1 # 흑
    arr[N//2][N//2] = 2 # 백
    dol_arr = deque()
    for i in range(1,M+1):
        dol = tuple(map(int,input().split()))
        dol_arr.append(dol)

    print(f'#{tc}',*oselo(arr))
