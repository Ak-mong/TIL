import sys
from collections import deque
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

# 20301 반전 요세풋스 실버 3
n,k,m = map(int,input().split())
deq = deque()
for x in range(1,n+1):
    deq.append(x)
# print(deq)
cnt = 0
cnt2 = 0
path = []
while deq:
    if cnt == k-1:
        a = deq.popleft()
        path.append(a)
        cnt2 += 1
        cnt = 0
    else:
        cnt += 1
        b = deq.popleft()
        deq.append(b)
    if cnt2 == m:
        deq.reverse()
        cnt2 = 0

for i in path:
    print(i)