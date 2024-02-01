import sys; sys.stdin = open('../txt/view.txt')
# 뭔가 에러가 나오는 중
T = 10
for tc in range(1, T+1):
    no = int(input())
    n = 100
    arr = [list(map(int, input().split())) for _ in range(n+1)]
    print(arr)
    # max_v = 0
    # # 행 우선
    # for i in range(n):
    #     total = 0
    #     for j in range(n):
    #         total += arr[i][j]
    #     # 최대값 변경
    #     if max_v < total:
    #         max_v = total
    # # 열 우선, 정사각형 행렬이기 때문에 가능
    # for i in range(n):
    #     total = 0
    #     for j in range(n):
    #         total += arr[j][i]
    #     # 최대값 변경
    #     if max_v < total:
    #         max_v = total
    # #  대각선 우선
    # total = 0
    # for i in range(n):
    #     total += arr[i][i]
    #     # 최대값 변경
    # if max_v < total:
    #         max_v = total
    # #  역 대각선 우선
    # total = 0
    # for i in range(n):
    #     total += arr[i][i]
    #     # 최대값 변경
    # if max_v < total:
    #         max_v = total
