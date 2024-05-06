# 14889 스타트와 링크 실버1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
# print(maps)
visited = [False] * (n+1)
sum_v = 1e10
def findindex(goal,level):
    global sum_v
    if goal == n//2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += maps[i][j]
                elif not visited[i] and not visited[j]:
                    link += maps[i][j]
        sum_v = min(sum_v,abs(start-link))
        return
    for i in range(level,n):
        if visited[i]: continue
        visited[i] = True
        findindex(goal+1,i+1)
        visited[i] = False
findindex(0,0)
print(sum_v)