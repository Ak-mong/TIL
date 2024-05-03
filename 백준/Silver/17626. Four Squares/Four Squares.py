import sys
input = sys.stdin.readline
import math

n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    min_v = i
    for j in range(1,int(math.sqrt(i))+1):
        min_v = min(min_v, dp[i-j*j])
    dp[i] = min_v + 1
print(dp[n])