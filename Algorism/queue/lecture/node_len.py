# 노드의 거리 문제
def bfs(s, N, G): # s : 시작정점 s, 노드 개수 N, 최단 거리 G
    q = []                      # 큐
    visited = [0] * (N+1)       # visited
    q.append(s)                 # 시작점 인큐
    visited[s] = 1              # 시작점 방문표시
    while q:                    # 처리안된 정점이 남아 있다면?
        x = q.pop(0)            # 처리할 정점 디큐:
        # x 에서 할 일
        if x == G:
            # 최단 경로 간선 수
            return visited[x] -1 # 시작정점에서 시작하기 때문에 1 뺀다
        for i in adjl[x]:
            if visited[i]:       # 인큐되지 않았으면(= 처리 된 적이 없으면)
                q.append(i)
                visited[i] = visited[x] +1
        return 0 # G 까지 경로가 없는 경우
T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    # 인접리스트
    adjl = [[] for _ in range(V+1)] # [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
    for i in range(E):
        n1, n2 = map(int,input().split())
        adjl[n1].append(n2)
    S, G = map(int,input().split())

    print(f'#{tc} {bfs(1, V, G)}')
