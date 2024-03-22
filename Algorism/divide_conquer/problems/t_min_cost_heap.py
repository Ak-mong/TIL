import sys;sys.stdin=open('min_cost.txt')
import heapq
def dijkstra(x,y):
    # 출발점 설정
    heap = []
    D[x][y] = 0
    heapq.heappush(heap, (D[x][y], x, y ))# 가중치, 좌표
    # 정점갯수만큼 반복
    # for _ in range(n*n):
    while heap:
        # 가중치 최소값인 정점 찾기
        d,x,y = heapq.heappop(heap)
        # 방문체크
        if visited[x][y]: continue
        if x == n-1 and y == n-1 : return

        # 인접정점 가중치 갱신
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] ==0:
                diff = 0
                if arr[nx][ny] > arr[x][y]: # 오르막일 때
                    diff = arr[nx][ny] - arr[x][y]
                if D[nx][ny] > D[x][y] + 1 + diff: # 갱신
                    D[nx][ny] = D[x][y] + 1 + diff
                    heapq.heappush(heap, (D[nx][ny], nx,ny))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = int(1e9)
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    D = [[INF] * n for _ in range(n)]   # 가중치
    visited = [[0] * n for _ in range(n)] # 방문체크
    dijkstra(0,0)
    print(f'#{tc} {D[n-1][n-1]}')

