import sys
sys.stdin = open("txt/view.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    height = list(map(int,input().split()))
    # 조망권을 위해서는 해당 세대의 왼쪽과 오른쪽에 둘다 2칸씩 없어야 된다.
    # 해당 세대의 갯수를 구해야된다.
    sum_v = 0
    for i in range(N-4):
        cnt = 0
        for j in range(i+1,N):
            pass
    print(f'#{tc} ')



