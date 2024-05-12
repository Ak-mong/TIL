import sys
input = sys.stdin.readline

# 브1 성지키기 1236
n,m= map(int,input().split())
arr = [list(input().strip()) for _ in range(n)]

a, b = 0, 0

for i in range(n):
    if "X" not in arr[i]:
        a += 1

for j in range(m):
    if "X" not in [arr[k][j] for k in range(n)]:
        b += 1

print(max(a,b))