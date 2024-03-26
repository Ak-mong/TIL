# 18917 수열과 쿼리 38 실버3
import sys
n = int(sys.stdin.readline())
results = 0
results4 = 0
for i in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    if arr[0] == 1:
        results += arr[1]
        results4 ^= arr[1]
    elif arr[0] == 2:
        results -= arr[1]
        results4 ^= arr[1]
    elif arr[0] ==3:
        print(results)
    elif arr[0] == 4:
        print(results4)