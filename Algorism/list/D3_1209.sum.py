import sys; sys.stdin = open('txt/sum.txt')

def sum_f():
    max_list = []
    # 가로 합
    max_j = 0  # 가로길이의 합
    for i in range(N):
        sum_j = 0
        for j in range(N):
            sum_j += arr[i][j]
        # print('sum_j',sum_j)
        if max_j < sum_j:
            max_j = sum_j
    max_list.append(max_j)
    # 세로합
    max_i = 0
    for j in range(N):
        sum_i = 0  # 세로길이의 합
        for i in range(N):
            sum_i += arr[i][j]
        if max_i < sum_i:
            max_i = sum_i
    max_list.append(max_i)
    # \ 대각선 합
    sum_lr = 0
    for i in range(N):
        sum_lr += arr[i][i]
    max_list.append(sum_lr)
    # / 대각선 합
    sum_rl = 0
    max_rl = 0
    for i in range(N-1,-1,-1):
        sum_rl += arr[N-1-i][i]
    max_list.append(sum_rl)
    return max(max_list)

N = 100
for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    sum_v = 0
    print(f'#{tc} {sum_f()}')
