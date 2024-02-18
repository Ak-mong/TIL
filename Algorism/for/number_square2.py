import sys;sys.stdin = open('txt/number_square.txt')
T = int(input())
for tc in range(1,T+1):
    H,W = map(int,input().split())
    # arr = [[0]*W for _ in range(H)] # 정사각형이 아니라서 사용못함
    print(f'#{tc}')
    for i in range(1,H+1):
        for j in range(W):
            print(i+H*j, end=' ')
        print()
