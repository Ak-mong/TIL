import sys
input = sys.stdin.readline

# N과 M 12 실버 2
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
path = []
dicts = {}
def find(level):
    if len(path) == m:
        if len(path) > 1:
            for i in range(len(path)-1):
                if path[i] > path[i+1]:
                    return
        paths = tuple(path)
        dicts[paths] = 1
        return
    for i in range(n):
        path.append(arr[i])
        find(i)
        path.pop()
find(0)
for p in dicts.keys():
    print(*p)