import sys
sys.stdin = open("../txt/number_card.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    a = int(input()) # 0 이 포함되면 0이 없어진다.
    # K = 인덱스 값 들 중 최대 값
    print(a)
    # arr =list(map(int, input()))
    # print(arr)
    cnts = [0] * 10
    # for i : 0->n-1
    for _ in range(N):
        cnts[a%10] +=1
        a = a //10
        print(a)
# 최대값 인덱스
    max_idx = 0
    # for i: 0 -> 0:
    for i in range(1, 10): #range(1,K+1)
        if cnts[max_idx] <= cnts[i]:
            max_idx = i
    print(f'#{test_case} {max_idx} {cnts[max_idx]}')