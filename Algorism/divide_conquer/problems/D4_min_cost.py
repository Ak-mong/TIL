import sys;sys.stdin = open('min_cost.txt')
import heapq

dij = [[0,1],[1,0],[0,-1],[-1,0]] # 오 밑

def find(y,x): # 시작점
    pq = []
    cnt = 0 # 갯수
    D[y][x] = 0
    heapq.heappush(pq, (D[y][x],y,x)) # 높이, 좌표 순 = 높이를 우선순위로 하기위함
    while pq: # q가 존재하는 동안
        h,y,x = heapq.heappop(pq)

        # 최소 높이로 이미 왔었다면
        if D[y][x] < h:
            continue
        # if visited[y][x]: continue
        # visited[y][x] = 1
        # sum_lens += h
        # print((y,x),h, end=' ')
        for k in range(4):
            dy = y + dij[k][0]
            dx = x + dij[k][1]
            if 0<= dy < n and 0<= dx < n: #벽체크
                # if visited[dy][dx] == 0: # 가본적이 없는 곳이라면
                if height[dy][dx] > height[y][x]:
                    sum_height = h + height[dy][dx] - height[y][x] + 1
                else:
                    sum_height = h + 1
                if sum_height >= D[dy][dx]: continue
                D[dy][dx] = sum_height
                # print(sum_height)
                heapq.heappush(pq,(D[dy][dx],dy,dx))

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    height = [ list(map(int,input().split())) for _ in range(n)]
    print(height)
    INF = int(1e9)
    D = [[INF] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    # print(find(0,0))
    find(0,0)
    print(D[n-1][n-1])
