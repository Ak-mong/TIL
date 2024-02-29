import sys;sys.stdin= open('txt/mirror')
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    move = 0
    # for x in arr:
    #     print(x)
    r,c = 0,0
    cnt = 0
    while 0 <= r < n and 0 <= c < n:
        if arr[r][c] == 2:
            if move%4 == 1 or move%4 == 3: #오왼->오->밑, 밑->위->왼
                move -= 1
            else:
                move += 1
            cnt +=1
        if arr[r][c] == 1:
            if move % 4 == 0 or move % 4 == 2:  # 밑-> 위-> 오, 위-> 밑->왼
                move -= 1
            else:
                move += 1
            cnt += 1
        if move%4 == 0: # 오
            c += 1
        elif move%4 == 1: # 밑
            r += 1
        elif move%4 == 2: # 왼
            c -=1
        elif move%4 == 3: # 위
            r -= 1
    print(f'#{tc} {cnt}')


