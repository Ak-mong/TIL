import sys;sys.stdin = open('fly.txt')
t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # print()
    # 한 칸씩
    result = []
    for i in range(n):
        for j in range(n):
            # 타격위치 + 영향
            kill_fly = 0
            for p in range(m):
                for q in range(m):
                    ni = i + p
                    nj = j + q
                    if 0<=ni<n and 0<=nj<n:
                        kill_fly += arr[ni][nj]
            # print(i,j,kill_fly)
            result.append(kill_fly)
    print(f'#{tc} {max(result)}')
