import sys;sys.stdin = open('txt/number_square2.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(1,N+1):
        for j in range(1,N+1):
            print(i*j, end=' ')
        print()