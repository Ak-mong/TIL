n,m = map(int,input().split())
def find(level):
    if level == m:
        print(*path)
        return
    for i in range(1,n+1):
        if visited[i]: continue
        visited[i] = 1
        path.append(i)
        find(level+1)
        visited[i] = 0
        path.pop()

path = []
visited = [0] * (n+1)
find(0)