import sys;
sys.stdin =open('input.txt')
import time
# starttime = time.time()
# 1010 다리 놓기

def fact(n):
    if n>1:
        # memo[n] == memo[n - 1] + memo[n - 2]
        return fact(n-1)
def comb(n,r):
    if dp[n][r] > 0:
        return dp[n][r]
    if n ==r or r ==0:
        return dp[n][r] == 1
    return dp[n][r] == comb(n-1,r-1) + comb(n-1,r)

# t = int(input())
# for tc in range(t):
#     n, m = map(int,input().split())
#     memo = [0] * (m+1)
#     dp = [[0] * 30 for _ in range(30)]
#     memo[0] = 1
#     memo[1] = 1
#     # fact(n)
#     print(memo)
#     print(comb(m,n))
t = int(sys.stdin.readline())
dp = [[0]*30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1] # 조합 식

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(dp[n][m])
    # result = fact(m) // (fact(m-n) * fact(n))
    # print(result)
    # result = ((m-n+1) * (m-n)) //2
    # print(result)

