import sys;sys.stdin = open('hanaro.txt')
from heapq import heappop, heappush
def prim(s):
    # 시작정점 설정
    total = 0
    pq = []
    D[s] = 0
    heappush(pq, (D[s],0)) # 가중치, 섬 번호

    while pq:
        # 최소 값
        d, v = heappop(pq)
        # 방문체크
        if visited[v]: continue
        visited[v] = 1
        total += dist[PI[v]][v] * tax_rate
        # 갱신
        for w in range(n): # 모든 정점이 연결된 완전 그래프
            if visited[w] == 0 and D[w] > dist[v][w]:
                D[w] = dist[v][w]
                PI[w] = v
                heappush(pq, (D[w], w))
    return total
t= int(input())
for tc in range(1,t+1):
    n = int(input())
    x_arr = list(map(int,input().split()))
    y_arr = list(map(int,input().split()))
    tax_rate = float(input())

    # 섬들간의 거리
    dist = [[0] * n for _ in range(n)]
    for i in range(n-1):
        for j in range(+1, n): # 조합 문제
            dist[i][j] = (x_arr[i] - x_arr[j]) ** 2 + (y_arr[i] - y_arr[j]) ** 2

    # 프림 변수들
    INF = int(1e9)
    D = [INF] * n # 가중치
    PI = [i for _ in range(n)]
    visited = [0] * n # 방문체크
    print(f'#{tc} {prim(0):.0f}')