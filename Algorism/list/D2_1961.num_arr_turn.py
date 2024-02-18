import sys; sys.stdin = open('txt/numarrturn.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(str,input().split())) for _ in range(N)]
    arr90 = [[0] * N for _ in range(N)]
    arr180 = [[0] * N for _ in range(N)]
    arr270 = [[0] * N for _ in range(N)]

    # 90 도
    for i in range(N):
        for j in range(N):
            arr90[j][N-1-i] = arr[i][j]
    # 180 도
    for i in range(N):
        for j in range(N):
            arr180[j][N - 1 - i] = arr90[i][j]
    # 270 도
    for i in range(N):
        for j in range(N):
            arr270[j][N - 1 - i] = arr180[i][j]
    print(f'#{tc}')
    for i in range(N):
        print(''.join(arr90[i]),''.join(arr180[i]),''.join(arr270[i]))