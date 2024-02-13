t = int(input())
# 첫번째 방법
def f(k):
    if k <= 1:
        return 1
    else:
        return f(k-1) + 2*f(k-2)
# 두번째 방법
memo = [1,1]
for i in range(2,31):
    memo.append((memo[i-1] + 2*memo[i-2]))

for tc in range(1,t+1):
    n = int(input()) // 10
    print(f'#{tc} {f(n)}')
    print(f'#{tc} {memo[n]}')
