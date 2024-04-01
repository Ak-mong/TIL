# 5014 스타트링크 실버 1
from collections import deque
f,s,g,u,d = map(int,input().split())
# 10층 건물로 이루어졌고 현재 1층이고 회사는 10층 한번에 2층 올라가고 1층 내려온다
# print(f,s,g,u,d)
flag = 0
visited = [0] * (f+1)
deq = deque()
deq.append(s)
visited[s] = 1
while deq:
    level = deq.popleft()
    if level == g:
        flag = 1
        break
    # if visited[level]: continue
    for x in [level+u, level-d]:
        if 0 < x <= f and visited[x] == 0:
            visited[x] = visited[level] +1
            deq.append(x)
if flag:
    print(visited[g]-1)
else:
    print('use the stairs')