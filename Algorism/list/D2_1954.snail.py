import sys; sys.stdin = open('txt/snail.txt')
dr = [0,1,0,-1]
dc = [1,0,-1,0]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]* N for _ in range(N)]
    # print(arr)

    r,c = 0,-1 #초기위치
    dist = 0 # 회전방향
    i = 1
    while i <= N*N:
        nr, nc = r + dr[dist], c + dc[dist]
        # 4방향 탐색 == 벽 체크
        if 0<= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            arr[nr][nc] = i
            i += 1 # 숫자 증가
            r, c = nr, nc
        # 벽에 부딪쳤다 or 도착한 곳이 0이 아니다
        else:
            dist = (dist + 1) % 4 # +1 씩 더해가다가 5이상 넘어가면 안되기 때문
    print(f'#{tc}')
    for x in arr:
        print(*x)