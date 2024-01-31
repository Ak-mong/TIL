"""
1 3 5 7 9
last = 1
1. 충전 못하는 경우
    if arr[i] - arr[i-1] < K:
        return 0

2. 충전을 하는 경우
    if arr[i] > last + k
        last = arr[i-1]
        cnt +=1
갈 때 마다 1,2번 두 번씩 비교해 나감
"""
k,n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
