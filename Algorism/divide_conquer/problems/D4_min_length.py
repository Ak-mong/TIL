import sys;sys.stdin=open('min_length.txt')

import heapq
def bfs(s):
    que = []
    # visited[s] = 1
    D[s] = 0
    heapq.heappush(que,(s,D[s]))
    while que:
        # 가중치 최소 값 찾기
        e, w = heapq.heappop(que)
        # 방문처리
        if visited[e]: continue
        visited[e] = 1

        # 인접 도시 업데이트
        for u in range(V+1): # 갈 수 있는 도시
            if adjl[e][u] and not visited[u]:
                if D[u] > D[e] + adjl[e][u]:
                    D[u] = D[e] + adjl[e][u]
                    heapq.heappush(que,(u,D[u]))

t= int(input())
for tc in range(1,t+1):
    V,E = map(int,input().split())
    adjl = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int,input().split())
        adjl[s][e] = w
    visited = [0] * (V+1)
    INF = int(1e9)
    D = [INF] * (V+1)
    # 함수 실행
    bfs(0)
    print(f'#{tc} {D[-1]}')
