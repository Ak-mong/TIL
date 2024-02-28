# 5C3
arr = ['a','b','c','d','e']
n = len(arr)
r = 3
path = []
def comb (level, start):
    if level == r:
        print(path)
        return
    for i in range(start,n):
        path.append(arr[i])
        comb(level+1, i+1)
        path.pop()
comb(0,0)