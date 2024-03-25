import sys;
sys.stdin =open('input.txt')
<<<<<<< HEAD

# 15652 N 과 M (4) 실버 3
# 중복 순열, 오른차순
def perm(level):
    if len(path) == m:
        print(*path)
        return
    for i in range(level,n+1):
        path.append(i)
        perm(i)
        path.pop()


n,m = map(int,input().split())
path = []
perm(1)
=======
import time
starttime = time.time()
>>>>>>> 4ec8326853acc8af0d9748dc098151cbdf5477f8

t = int(input())
for tc in range(1,t+1):
    n = float(input())
    str = ''
    while n != 0:
        n *= 2
        if n >= 1:
            n -= 1
            str += '1'
        elif n < 1:
            str += '0'
        if len(str) > 12:
            str = 'overflow'
            break
    print(str)

