import sys
from collections import deque
input = sys.stdin.readline
# 1697 숨바꼭질 실버 1
# T/F 식 풀이

def bfs(v):
    global min_cnt
    deq = deque()
    deq.append((v,0))
    while deq:
        value,cnt = deq.popleft()
        if value == k:
            if min_cnt > cnt:
                min_cnt = cnt
                break
        for i in [value * 2, value + 1, value - 1]:
            if 0 <= i <= int(1e5) and not visited[i]:
                visited[i] = True
                deq.append((i, cnt+1))


n,k = map(int,input().split())
visited = [False] * 100001
min_cnt = int(1e10)
bfs(n)
print(min_cnt)
