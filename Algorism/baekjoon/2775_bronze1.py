import sys;sys.stdin =open('input.txt')
'''
k층 n호에 몇명이 살고있을까
k층의 n호에는 (k-1)층의 1~n호까지 사는 사람들의 합이 산다
'''

t = int(input())
for tc in range(t):
    k = int(input())
    n = int(input())
    memo = [[0] * (n+1) for _ in range(k+1)]
    for i in range(1,n+1):
        memo[0][i] = i
    for x in range(1,k+1):
        sum_v = 0
        for y in range(1,n+1):
            sum_v += memo[x-1][y]
            memo[x][y] = sum_v
    # print(memo)
    print(memo[k][n])