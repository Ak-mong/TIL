import sys
sys.stdin = open("txt/number_card.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    a = int(input())
    arr = []
    for i in range(N):
        arr.append(a % 10)
        a = a // 10
    # print(arr)
    cnt = [0] * 10
    max_v = 0
    max_i = 0
    for i in range(N):
        cnt[arr[i]] += 1

    for i in range(10):
        if cnt[max_i] <= cnt[i]:
            max_i = i
    # print(cnt)
    # print(cnt[max_i])
    # print(max_i)
    print(f'#{test_case} {max_i} {cnt[max_i]}')
