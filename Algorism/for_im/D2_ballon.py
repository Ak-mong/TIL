import sys;sys.stdin = open('ballon.txt')
dij = [(0,1),(1,0),(0,-1),(-1,0)]
t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            ij_sum = arr[i][j]
            for k in range(4):
                for p in range(1,arr[i][j]+1):
                    ni,nj = i + dij[k][0]*p , j + dij[k][1]*p
                    if 0<=ni<n and 0<=nj<m: # 벽체크
                        ij_sum += arr[ni][nj]
            result.append(ij_sum)
    print(f'#{tc} {max(result)}')
