"""
V, E : V 1~V 까지 V개의 정점. E개의 간선
E개의 간선정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def bfs(v):
    visited = [0] * (V+1)
    q = [v]
    # enQ 방문체크
    visited[v] = 1
    #
    while q:
        r = q.pop(0) # deQ
        # 인접하고 미방문 -> enQ
        for w in adjl[r]:
            if not visited[w]: # 미 방문한 친구
                q.append(w)
                visited[w] = visited[r] + 1
    print(visited.index(max(visited)),max(visited))


V, E = map(int,input().split())
tmp = list(map(int,input().split()))
# 인접리스트
adjl = [[] for _ in range(V+1)]
for i in range(E):
    s, e = tmp[2*i], tmp[2*i+1]
    adjl[s].append(e)
    adjl[e].append(s)
bfs(1)
# 1번 정점에서 가장 멀리 떨어져 있는 정점번호와 거리(간선의 갯수)를 출력하시오.