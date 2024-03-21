import sys;
sys.stdin =open('input.txt')
import time
# starttime = time.time()

# 15651 n과 m (3)
'''
중복 순열
'''
def dfs(level):
    if level == m:
        print(*path)
        return
    for i in range(1, n + 1):
        if visited[i]: pass
        visited[i] = 1
        path.append(i)
        dfs(level+1)
        path.pop()
        visited[i] = 0

n,m = map(int,input().split())
visited = [0] * (n+1)
path = []
dfs(0)