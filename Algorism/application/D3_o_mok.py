import sys;sys.stdin=open('txt/o_mok.txt')


def o_mok():
    flag = 0
    # 가로
    for i in range(n):
        for j in range(n):
            if j +4 > n: break
            if j + 4 < n and arr[i][j] == 'o' and arr[i][j + 1] == 'o' and arr[i][j + 2] == 'o' and arr[i][j + 3] == 'o' and arr[i][j + 4] == 'o':
                flag = 1
                return flag
    # 세로
    for i in range(n):
        for j in range(n):
            if i+4 > n: break
            if i + 4 < n:
                if arr[i][j] == 'o' and arr[i + 1][j] == 'o' and arr[i + 2][j] == 'o' and arr[i + 3][j] == 'o' and arr[i + 4][j] == 'o':
                    flag = 1
                    return flag
    # 역 대각선으로 보기
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if i + 4 > n and j - 4 <= 0: break
            if i + 4 < n and j - 4 >= 0:
                if arr[i][j] == 'o' and arr[i + 1][j - 1] == 'o' and arr[i + 2][j - 2] == 'o' and arr[i + 3][j - 3] == 'o' and arr[i + 4][j - 4] == 'o':
                    flag = 1
                    return flag
    # 정 대각선
    for i in range(n):
        for j in range(n):
            if i + 4 > n and j + 4 > n: break
            if i + 4 < n and j + 4 < n:
                if arr[i][j] == 'o' and arr[i + 1][j + 1] == 'o' and arr[i + 2][j + 2] == 'o' and arr[i + 3][j + 3] == 'o' and arr[i + 4][j + 4] == 'o':
                    flag = 1
                    return flag
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    stack = [0 for _ in range(4)] # 가로 세로 대각 역대각
    # print(f'#{tc}')
    # for x in arr:
    #     print(x)
    if o_mok():
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

    # print(stack)
