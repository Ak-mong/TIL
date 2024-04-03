import sys
from collections import deque
sys.stdin =open('input.txt')
input = sys.stdin.readline
# 1389 케빈 베이컨의 6단계 법칙 실버1
from collections import deque

import sys
input = sys.stdin.readline
# 4803  트리 골드 4
n,m= map(int,input().split())
# n 정점의 개수, m 간선의 개수
adjl = [[] for _ in range(n+1)]
for i in range(m):
    s,e = map(int,input().split())
    adjl[s].append(e)
    adjl[e].append(s)

print(adjl)
path = []
visited = [0] * (n+1)
visited[1] = 1
def dfs(level):
    if len(path) == n:
        print(path)
    for i in adjl[level]:
        if visited[i]: continue
        path.append(i)
        dfs(i)
        path.pop()


dfs(1)