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
    for i in range(2, N-2):
        max_v = 0
        # cnt = 0
        for j in range(i-2,i+3):
            if j != i:
                if max_v < height[j]:  # min_v 가 더 작을 때
                    max_v = height[j]
        if height[i] > max_v:
            sum_v += height[i] - max_v
    # sum_v = 0
    # for i in range(2, N-2):
    #     max_v = max([height[i-2], height[i-1], height[i+1], height[i+2] ] )
    #     if height[i] >= max_v:
    #         sum_v += height[i] - max_v
        # print(max_v)
    print(f'#{tc} {sum_v}')



