# 브론즈 2
n = int(input())
arr = list(map(int,input().split()))
prime = [1] * 1001
prime[1] = 0
for i in range(2,1001):
    if prime[i]:
        for j in range(2*i,1001,i):
            prime[j] = 0
cnt = 0
for x in arr:
    if prime[x]:
        cnt += 1
print(cnt)
