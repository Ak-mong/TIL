# 5C3
arr = ['a','b','c']
n = len(arr)
r = 2
path = []
def comb (level, start):
    if level == r:
        print(path)
        return
    for i in range(start,n):
        path.append(arr[i])
        comb(level+1, i)
        path.pop()
comb(0,0)