#메모리제이션이 아니라 메모이제이션이 맞다
def fibo(n):
    global cnt
    cnt += 1
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

cnt = 0
print(fibo(7),'횟수:', cnt)

# 메모이제이션
def fibo_memo(n):
    global cnt_memo
    cnt_memo += 1
    if n!=0 and memo[n] ==0:
        memo[n] = fibo_memo(n-1)+fibo_memo(n-2)
    return memo[n]

cnt_memo = 0
n = 7
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
print(fibo_memo(n),'횟수:',cnt_memo)
print(memo[n]) # 이렇게 해도 됨
print(memo) # 파보나치 리스트 호출
