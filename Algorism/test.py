import sys;
sys.stdin =open('input.txt')
import time
# starttime = time.time()

n,m = map(int,input().split())
def find(level):
    if level == m:
        print(path)
        return
    for i in range(n):
        if visited[i]:
            visited[i] = 1
            path.append(i)
            visited[i] = 0
            path.pop()

path = []
visited = [0] * n
find(0)

