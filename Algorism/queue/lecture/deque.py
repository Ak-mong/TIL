from collections import deque
import time
start_time = time.time()

q = deque()
q.append(1)
q.append(2)
print(q.popleft())
print(q.popleft())

q1 = []
for i in range(100000000):
    q1.append(i)
print(
    'append'
)
while q1:
    q1.pop(0)
print('end')
print(start_time-time.time())

dq = deque()
for i in range(100000000):
    dq.append(i)
print(
    'append'
)
while q:
    dq.popleft()
print('end')
print(start_time - time.time())