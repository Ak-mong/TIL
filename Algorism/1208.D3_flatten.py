import sys
sys.stdin = open("txt/flatten", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = [0] * len(arr)
    print(max(arr))
    print(arr)
    for i in range(len(arr)):
        cnt[arr[i]] += 1
    print(cnt)
    # print(f'#{tc} {sum_v}')



