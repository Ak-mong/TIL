import sys
input = sys.stdin.readline
# 1389 케빈 베이컨의 6단계 법칙 실버1
from collections import deque

def dfs(level, curcnt, goal):
    global min_cnt
    if level == goal:
        # print('level',goal,curcnt)
        if min_cnt > curcnt:
            if min_cnt != 1e10: lists.pop()
            min_cnt = curcnt
            lists.append(curcnt)
            # print(level,lists)
            return curcnt
    if visited[level]: return
    visited[level] = 1
    for k in range(len(adjl[level])):
        if adjl[level][k] ==1:
            dfs(k,curcnt+1,goal)
    return curcnt

n, m = map(int,input().split())
adjl = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    s, e = map(int,input().split())
    # adjl[s].append(e)
    # adjl[e].append(s)
    adjl[s][e] = 1
    adjl[e][s] = 1

# for p in adjl:
#     print(p)
min_v = 1e10
min_i = n
for i in range(1,n+1): # 1~n까지 돌리기
    sum_v = 0
    lists = []
    for j in range(1,n+1):
        if i == j: continue
        min_cnt = 1e10
        visited = [0] * (n+1)
        cnt = 0
        dfs(i,0,j)
    # print(sum(lists))

    if min_v > sum(lists):
        min_v = sum(lists)
        min_i = i
            # min_i = i
# print('v',min_v)
print(min_i)