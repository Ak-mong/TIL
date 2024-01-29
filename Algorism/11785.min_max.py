import sys
sys.stdin = open("txt/min_max_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())
    num = list(map(int, input().split()))
    min_v = max_v = num[0]
    for i in range(N):
        if min_v > num[i]:
            min_v = num[i]
        if max_v < num[i]:
            max_v = num[i]
    print(f'#{test_case} {max_v - min_v}')

    # ///////////////////////////////////////////////////////////////////////////////////
