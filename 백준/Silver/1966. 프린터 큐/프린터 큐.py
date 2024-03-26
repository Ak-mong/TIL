# 1966 프린터 큐 실버3
from collections import deque
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    prioritys = list(map(int,input().split()))
    priority = deque()
    for i in range(len(prioritys)):
        priority.append((i,prioritys[i]))
    # print(priority)
    cnt = 0
    while priority:
        if priority[0][1] == max(priority, key=lambda x:x[1])[1]:
            cnt += 1
            if priority[0][0] == m:
                print(cnt)
                break
            else:
                priority.popleft()
        else:
            priority.append(priority.popleft())