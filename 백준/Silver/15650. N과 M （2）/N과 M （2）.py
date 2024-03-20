n,m = map(int,input().split())
path = []
path_wrap = []
visited = [False] * (n+1)
def perm(level):
    if level ==m:
        paths = path[:]
        paths.sort()
        if paths not in path_wrap:
            path_wrap.append(paths)
        return
    for i in range(1,n+1):
        if visited[i]: continue
        visited[i] = True
        path.append(i)
        perm(level+1)
        path.pop()
        visited[i] = False

perm(0)
for i in path_wrap:
    print(*i)