import sys;sys.stdin = open('dongchul.txt')

'''
n명의 직원
해야할 일 n개
i 번 직원이 j번 일할 확률 Pij
'''
def perm(level,cursum):
    global max_v, cnt
    if max_v > cursum or cursum == 0: return
    cnt += 1
    if level == n:
        # 할 일
        if max_v < cursum: max_v = cursum
        # print(path)
        return
    for i in range(n):
        if used[i]: continue
        used[i] = 1
        perm(level+1, cursum * arr[level][i]/100)
        used[i] = 0

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    path = []
    used = [0] * n
    max_v = -1
    cnt = 0
    perm(0,1)
    print(f'#{tc} {max_v*100:.6f}')
    print(cnt)