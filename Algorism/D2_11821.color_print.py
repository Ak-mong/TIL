import sys , pprint
sys.stdin = open("txt/color_print.txt","r")
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = [[0] * 10 for _ in range(10)]

    count = 0
    for a in range(len(arr)):
        r1 = arr[a][0]
        c1 = arr[a][1]
        r2 = arr[a][2]
        c2 = arr[a][3]
        color = arr[a][4]
        for i in range(r1, r2+1):
            for j in range(c1,c2+1):
                if cnt[i][j] == 0:
                    cnt[i][j] = color
                elif cnt[i][j] != color:
                    cnt[i][j] = 3
        purple = 0
        for x in range(10):
            for y in range(10):
                if cnt[x][y] == 3:
                  purple += 1
    print(f'#{tc} {purple}')