import sys;sys.stdin =open('txt/sdoku.txt')
def sdokuOK(sdoku):
    for i in range(0,9,3):
        for j in range(0,9,3):
            lst_3 = [0] * 10
            for p in range(3):
                for q in range(3):
                    # 3x3 ok?
                    lst_3[sdoku[i+p][j+q]] += 1
                    if lst_3[sdoku[i+p][j+q]] ==2:
                        return 0
    for x in range(9):
        lst_row = [0] * 10
        lst_col = [0] * 10
        for y in range(9):
            lst_row[sdoku[x][y]] +=1
            lst_col[sdoku[y][x]] +=1
            # 가로 ok?
            if lst_row[sdoku[x][y]] ==2:
                return 0
            # 세로 ok?
            if lst_col[sdoku[y][x]] ==2:
                return 0
    return 1
t = int(input())
for tc in range(1,t+1):
    n = 9
    sdoku = [list(map(int,input().split())) for _ in range(9)]
    print(f'#{tc} {sdokuOK(sdoku)}')

