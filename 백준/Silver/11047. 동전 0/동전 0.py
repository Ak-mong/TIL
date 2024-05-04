import sys
input = sys.stdin.readline

# 11047 동전 0 실버 4
n,k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
i = n-1
cnt = 0
while k >=0 and i >=0:
    if k >= arr[i]:
        cnt += k // arr[i]
        k %= arr[i]
    i -= 1
print(cnt)