import sys;sys.stdin = open('txt/pascal.txt')

T = int(input())
Size = 10 + 1
memo = [[0] * Size for _ in range(Size)]
for i in range(Size):
    for j in range(Size):
        if j ==0 or i==j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i-1][j] + memo[i-1][j-1]
# print(memo)
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(memo[i][j], end= ' ')
        print()