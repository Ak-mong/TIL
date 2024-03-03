import sys;sys.stdin=open('sdoku.txt')

'''

'''
def sdoku_test():
    # 9칸 검사
    for k in range(0, 9, 3):
        cnt9 = [0] * 10
        for i in range(3):
            for j in range(3):
                cnt9[arr[k + i][k + j]] += 1
                if cnt9[arr[k + i][k + j]] >=2:
                    return 0
    # 가로,세로 검사
    for x in range(9):
        cnt_r = [0] * 10
        cnt_c = [0] * 10
        for y in range(9):
            cnt_c[arr[x][y]] += 1
            if cnt_c[arr[x][y]] >=2:
                return 0
            cnt_r[arr[y][x]] += 1
            if cnt_r[arr[y][x]] >= 2:
                return 0

    return 1
t= int(input())
for tc in range(1,t+1):
    arr = [list(map(int,input().split())) for i in range(9)]
    print(f'#{tc} {sdoku_test()}')