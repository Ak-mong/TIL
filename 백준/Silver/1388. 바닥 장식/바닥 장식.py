import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 1388 바닥장식 실버 4
n,m = map(int,input().split())
arr = [list(input().strip()) for _ in range(n)]
cnt = 0
def dfs1(r,c):
    global cnt
    arr[r][c] = '.'
    nc = c + 1
    if nc < m:
        if arr[r][nc] == '-':
            dfs1(r,nc)
        else:
            cnt += 1
            return
    else:
        cnt += 1

def dfs2(r,c):
    global cnt
    arr[r][c] = '.'
    nr = r + 1
    if nr < n:
        if arr[nr][c] == '|':
            dfs2(nr,c)
        else:
            cnt += 1
            return
    else:
        cnt += 1
        return

for i in range(n):
    for j in range(m):
        if arr[i][j] == '-':
            dfs1(i,j)
        elif arr[i][j] == '|':
            dfs2(i,j)
print(cnt)