import sys;sys.stdin = open('txt/str_square.txt')
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(n-1, -1, -1):
            arr[j][i] = chr(65 + (n-1-j)+(n-1-i)*n)
            # arr[i][j] = 1
    print(f'#{tc}')
    for x in arr:
        print(*x)
