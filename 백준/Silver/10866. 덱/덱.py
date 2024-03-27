import sys
from collections import deque
# 10866  덱 실버4

n = int(input())
d = deque()
for _ in range(n):
    input_v = sys.stdin.readline().split()
    v = input_v[0]
    if v =='push_front':
        d.appendleft(input_v[1])
    elif v == 'push_back':
        d.append(input_v[1])
    elif v == 'pop_front':
        if d: print(d.popleft())
        else: print(-1)
    elif v == 'pop_back':
        if d: print(d.pop())
        else: print(-1)
    elif v == 'size':
        print(len(d))
    elif v == 'empty':
        if d: print(0)
        else: print(1)
    elif v == 'front':
        if d: print(d[0])
        else: print(-1)
    elif v=='back':
        if d: print(d[-1])
        else: print(-1)
