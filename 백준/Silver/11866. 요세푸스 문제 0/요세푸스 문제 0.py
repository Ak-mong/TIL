import sys
from collections import deque
input = sys.stdin.readline
# 11866 요세푸스 문제 0 실버5
n,k = map(int,input().split())
deq = deque()
for p in range(1,n+1):
    deq.append(p)
cnt = 0
path = []
while deq:
    if cnt == k-1:
        b = deq.popleft()
        cnt = 0
        path.append(b)
    else:
        cnt += 1
        a = deq.popleft()
        deq.append(a)
print('<', end='')
for i in range(n):
    if i == n-1: print(path[i], end='')
    else: print(path[i], end = ', ')

print('>', end='')