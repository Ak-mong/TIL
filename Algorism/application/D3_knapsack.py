import sys;sys.stdin=open('txt/knapsack.txt')
'''
배낭에 담을 수 있는 총 무게 = k
창고에 n개의 물건, 각 물건에 무게 v 가치 c
배낭이 수용하는 부피 k
가치 최대
물건 못 쪼갬
'''
def bitFun(x):
    global sum_v
    sum_v = 0
    sum_w = 0
    for i in range(n):
        if x & 0x1: #
            # print(arr[i][0], end=' ')
            sum_w += arr[i][0]
            sum_v += arr[i][1]
        x >>= 1
    return sum_w
    # print()
t = int(input())
for tc in range(1,t+1):
    n,k = map(int,input().split()) # 개수 부피
    arr = [list(map(int,input().split())) for _ in range(n)] # 무게, 가치
    bit = [0] * n
    sum_v = 0
    v_list = []

    for i in arr:
        v = i[0]
        c = i[1]
    for j in range(1<<n):
        if bitFun(j) <= k:
            v_list.append(sum_v)
    print(v_list)

    print(f'#{tc} {max(v_list)}')