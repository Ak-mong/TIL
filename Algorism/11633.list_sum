import sys
sys.stdin = open("txt/list_sum.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N, M = list(map(int,input().split()))
    a = list(map(int,input().split()))
    x_lst = []
    for i in range(N-M+1):
        x = 0
        for j in range(M):
            x += a[i+j]
        x_lst.append(x)
    print(f'#{tc} {max(x_lst) - min(x_lst)}')



