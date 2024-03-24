from collections import deque
# 2164 카드 2 실버4
n = int(input())
arr = deque()
for i in range(1,n+1):
    arr.append(i)

while len(arr) > 1:
    arr.popleft()
    a =arr.popleft()
    arr.append(a)
print(*arr)