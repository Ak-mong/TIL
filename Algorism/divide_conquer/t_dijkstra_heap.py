# 최단 경로
import sys;sys.stdin = open('input.txt')
'''
서울(0), 천안(1), 원주(2), 논산(3), 대전(4),
대구(5), 강릉(6), 광주(7), 부산(8), 포항(9)
'''
'''
9 14
0 1 12
0 2 15
1 3 4
1 4 10
2 5 7
2 6 21
3 4 3
3 7 13
4 5 10
5 8 9
5 9 19
6 9 25
7 8 15
8 9 5
'''
import heapq
def dijkstra(s):
    # 출발점 설정
    pq = []
    D[s] = 0
    heapq.heappush(pq,(D[s],s)) # (가중치, 도시)

    while pq:
        # 가중치 최소 값 찾기
        wt, v = heapq.heappop(pq)

        # 방문 처리
        if visited[v]: continue # 찾기 심힘
        visited[v] = 1 # 다음번에 찾을 때 다시 안 구하기 위해서

        # 인접도시 업데이트
        for w in range(V+1):
            if adj[v][w] and not visited[w]:
                if D[w] > D[v] + adj[v][w]:
                    D[w] = D[v] + adj[v][w]
                    heapq.heappush(pq,(D[w],w))

V, E = map(int,input().split())
adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
INF = int(1e9)
D = [INF] *(V+1)                # 가중치
visited = [0] * (V+1)           # 방문

for i in range(E):
    s, e, w = map(int,input().split()) # 시작 , 끝,  가중치
    adj[s][e] = adj[e][s] = w          # 무향 그래프라서
dijkstra(0)
print(D)
