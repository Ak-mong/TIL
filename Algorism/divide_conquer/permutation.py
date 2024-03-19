# 순열
def perm(level):
    if level == r:
        print(path)
        return
    for i in range(n):
        if used[i]: continue
        used[i] = 1
        path.append(arr[i])
        perm(level+1)
        path.pop()
        used[i] = 0



arr = [1,2,3]
n = len(arr)
r = 3
path = []
used = [0] * n
perm(0)