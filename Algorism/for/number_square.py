import sys;sys.stdin = open('txt/number_square.txt')
T = int(input())
for tc in range(1,T+1):
    H,W = map(int,input().split())
    print(f'#{tc}')
    for i in range(0,H*W,W):
        for j in range(1,W+1):
            print(i+j, end=' ')
        print()
