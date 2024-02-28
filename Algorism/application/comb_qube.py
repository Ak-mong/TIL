'''
주사위 3개
모든 조합
'''
n = 3
path = []
def qube(lev,start):
    if lev == n:
        print(path)
        return

    for i in range(start,7):
        path.append(i)
        qube(lev+1,i)
        path.pop()

qube(0,1)