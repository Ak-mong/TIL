import sys
from collections import deque
input = sys.stdin.readline

# 1158 요세푸스 문제 실버4
n,k = map(int,input().split())
deq = deque()
for i in range(1,n+1):
    deq.append(i)
path = []
cnt = 0
while deq:
    if cnt == k-1:
        a = deq.popleft()
        path.append(a)
        cnt = 0
    else:
        cnt += 1
        b = deq.popleft()
        deq.append(b)
# print(path)
print('<', end='')
for j in range(n):
    if j == n-1:
        print(path[j], end='')
    else:
        print(path[j], end=', ')
print('>', end='')