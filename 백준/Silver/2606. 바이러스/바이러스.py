# 2606 바이러스 실버3
from collections import deque
computer = int(input())
network = int(input())
adjl = [[] for _ in range(computer+1)]
for _ in range(network):
    s,e = map(int,input().split())
    adjl[s].append(e)
    adjl[e].append(s)
def bfs(v):
    deq = deque()
    deq.append(v)
    visited = [0] * (computer + 1)
    visited[v] = 1
    cnt = 0
    while deq:
        value = deq.popleft()
        for i in range(1,computer+1):
            if not visited[i] and i in adjl[value]:
                visited[i] = visited[value] + cnt
                cnt += 1
                deq.append(i)
    return cnt

print(bfs(1))