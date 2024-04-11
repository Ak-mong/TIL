import sys
input = sys.stdin.readline

# 1929 소수 구하기 실버3
m,n = map(int,input().split())
prime = [True] * (n+1)
for i in range(2,n+1):
    for j in range(2*i,n+1,i):
        prime[j] = False

for i in range(m,n+1):
    if prime[i] and i != 1:
        print(i)