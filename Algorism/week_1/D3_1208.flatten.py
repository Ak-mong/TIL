import sys
sys.stdin = open("txt/flatten", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))

    # cnt = [0] * len(arr)
    # print(max(arr))
    # print(arr)
    # for i in range(len(arr)):
    #     cnt[arr[i]] += 1
    # print(cnt)
    max_v = min_v = 0
    for i in range(N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]
        max_v -= 1
        min_v -= 1
    print(max_v - min_v)
    # print(f'#{tc} {sum_v}')

    # 평탄화 작업 반복문
    for _ in range(N):
        max_i = 0
        min_i = 0
        for i in range(len(arr)):
            if arr[max_i] < arr[i]:
                max_i = i
            if arr[min_i] > arr[i]:
                min_i = i
        arr[max_i] -= 1
        arr[min_i] += 1

    # 평탄화가 완료 된 후 max 랑 min 찾기가 한번 더 이루어져야 함
    for i in range(len(arr)):
        if arr[max_i] < arr[i]:
            max_i = i
        if arr[min_i] > arr[i]:
            min_i = i
    print(f'#{tc} {arr[max_i] - arr[min_i]}')
"""
    max_v = 0
    min_v = 101
    min_i = -1
    max_i = -1
    for i in range(len(arr)):
        if max_v < arr[i]:
            max_v = arr[i]
            max_i = i
        if min_v > arr[i]:
            min_v = arr[i]
            min_i = i
    x = 0
    while x < N:
        arr[max_i] -= 1
        arr[min_i] ++ 1
        x += 1

    print(f'#{tc} {arr[max_i] - arr[min_i]}')
    """
"""    cnt = [0] * 101
    # print(arr)
    for i in arr:
        cnt[i] += 1
    max_v = min_v = arr[1]
    for i in arr:
        if max_v < i:
            max_v = i
        if min_v > i:
            min_v = i
    x = 0
    while  x< N:
        cnt[max_v] -= 1
        cnt[min_v] += 1
        if cnt[max_v] == 0:
            max_v -= 1
        if cnt[min_v] == N:
            min_v += 1
        x +=1
    print(max_v - min_v)
    """





