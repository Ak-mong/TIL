# 1003 파보나치 실버3
def fibonacci(n):
    global cnt_0,cnt_1
    for i in range(n+1):
        if i ==0:
            memo[0] = 0
        elif i == 1:
            memo[1] = 1
        else:
            memo[i] = memo[i-1] + memo[i-2]

t = int(input())
for _ in range(t):
    m = int(input())
    memo = [0] * (m+1)
    fibonacci(m)
    if len(memo) == 1:
        cnt_0 = 1
        cnt_1 = 0
    elif len(memo) <=2:
        cnt_0 = memo[0]
        cnt_1 = memo[1]
    else:
        cnt_0 = memo[-2]
        cnt_1 = memo[-1]
    # print(memo)
    print(cnt_0,cnt_1)