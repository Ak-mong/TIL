import sys; sys.stdin = open('txt/spin.txt')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    stack = [0] * N*M
    # print(stack)

    front = rear = -1
    for i in range(M+1):
        rear += 1
        stack[rear] = arr[rear % N]
    print(stack)
    print(f'#{tc} {stack[M]}')
