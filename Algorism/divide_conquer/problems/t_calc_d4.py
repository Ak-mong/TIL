import sys;sys.stdin=open('calc.txt')


def bfs(n,m):
    Q = [n]
    visited[n] = 1
    while Q:
        v = Q.pop(0)
        if v==m:
            return visited[m] - 1
        for w in [v+1,v-1,v*2,v-10]:
            if 0<w <= 1_000_000:# 백만 이하의 자연수
                if visited[w] ==0:
                    visited[w] = visited[v] + 1
                    Q.append(w)

t = int(input())
for tc in range(1,t+1):
    N,M = map(int,input().split())
    visited = [0] * (1_000_000 + 1)
    print(f'#{tc} {bfs(N,M)}')