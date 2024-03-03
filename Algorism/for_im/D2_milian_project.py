import sys;sys.stdin=open('milian.txt')

'''
최대값을 구하고,
최대값과의 차이가 
-1 -1 
6
리스트를 가면서 맥스값을 발견했다면 그 때 전부 판매
그리고 나서 판매
while? for?
1 1 3 1 2

'''
t= int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    len_arr = len(arr)
    sum_v = 0
    # 최대값을 찾고
    start = 0 #
    buy_sum = 0
    cnt = 0
    max_v = 0
    max_i = 0
    while max_i < n:
        for i in range(start,n):
            if max_v < arr[i]:
                max_v = arr[i]
                max_i = i
        # start부터 max_i 까지 더해나가기
        for j in range(start,max_i):
            buy_sum += arr[j]
            cnt += 1

        sum_v += (arr[max_i] * cnt - buy_sum)
        buy_sum = cnt = max_v = 0  # 초기화
        start = max_i + 1

        if max_i == n-1:
            break

    print(f'#{tc} {sum_v}')


