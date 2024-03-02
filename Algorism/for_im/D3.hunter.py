import sys;sys.stdin=open('hunter.txt')

drc = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]# 63214789

t= int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                for k in range(8):
                    c = 1
                    while c<n:
                        ni = i + drc[k][0] * c
                        nj = j + drc[k][1] * c
                        if ni < 0 or nj < 0 or n <= ni or n <= nj or arr[ni][nj] == 3 or arr[ni][nj] == 1:
                            break
                        if arr[ni][nj] == 2:
                            arr[ni][nj] = 9
                        c += 1
    cnt = 0
    for p in range(n):
        for q in range(n):
            if arr[p][q] == 9:
                cnt += 1
    print(f'#{tc} {cnt}')
    # for b in arr:
    #     print(b)