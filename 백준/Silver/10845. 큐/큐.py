import sys
input = sys.stdin.readline

# 10845 큐 실버4
n = int(input())
path = []
for i in range(n):
    a = list(input().split())
    if a[0] == 'push':
        path.append(a[1])
    elif a[0] == 'pop':
        if path:
            b = path.pop(0)
            print(b)
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(path))
    elif a[0] == 'empty':
        if path: print(0)
        else: print(1)
    elif a[0] == 'front':
        if path: print(path[0])
        else: print(-1)
    elif a[0] == 'back':
        if path: print(path[-1])
        else: print(-1)