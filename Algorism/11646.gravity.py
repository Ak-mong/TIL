import sys
sys.stdin = open("txt/gravity.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    # 오른쪽으로 자기보다 낮은 애들의 갯수 = 떨어질 수 있는 높이, 이것의 최대값을 구해야된다.
    max_val = 0 #max_val 을 초기화
    # for i:0 -> N-1, N개니까 index는 0~n-1 낙차 구하는 위치
    for i in range(N-1): # 기준이 되는 막대기 오른쪽으로의 막대기 갯수 만큼 돌아라 N-1~0개 = N-1개 만큼
        cnt = 0 # cnt 초기화
        # for j : i+1 ~ n-1 까지 각 막대기의 갯수
        for j in range(i+1,N): #range(숫자) 가 아니기 때문에, i+1~N = N-i-1개
            if arr[i] > arr[j]: # 기준(i)이 되는 막대의 블럭 개수가 비교(j)하는 막대의 블럭 개수보다 클 때만
                cnt += 1 # cnt를 하나씩 추가시킨다.
        if max_val < cnt: # 가장 낙차가 큰 값(max_val) 이 cnt 보다 작을 때
            max_val = cnt # 교체한다.
    pass
    print(f'#{tc} {max_val}')



