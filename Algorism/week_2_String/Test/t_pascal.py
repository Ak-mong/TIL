import sys;sys.stdin = open('../txt/pascal.txt')

SIZE = 10+1
memo = [[0] * SIZE for _ in range(SIZE)]
for i in range(SIZE):
    for j in range(SIZE):
        if j == 0 or i ==j: # 돌렸을 때 1이 되는 경우
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]


T = int(input())
for tc in range(1,T+1):
    N = int(input())

    # 출력
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(memo[i][j], end=' ')
        print()