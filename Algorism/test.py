import sys;
sys.stdin =open('input.txt')

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


