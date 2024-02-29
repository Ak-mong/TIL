import sys;sys.stdin=open('txt/o_mok.txt')
dy = [1,0,1,-1] # 아 오 대각, 역대각
dx = [0,1,1,1]
def o_mok(y,x):
    # 4방향 탐색
    for bang in range(4):
        cnt = 1 # 기준 좌표에 돌이 있다 cnt = 1부터 시작
        # 돌 4개를 탐색
        for power in range(1, 5):
            ny = y + (dy[bang] * power)
            nx = x + (dx[bang] * power)
            if not (0 < ny <= n and 0 < nx <= n): break
            # 돌을 발견하면 count
            if arr[ny][nx] == 'o': cnt += 1
            if cnt == 5:  # 오목 발견
                return True
    return False
def game_start():
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 'o':
                if o_mok(r,c):
                    return 'YES'
    return 'NO'


t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    result = game_start()
    print(f'#{tc} {result}')

