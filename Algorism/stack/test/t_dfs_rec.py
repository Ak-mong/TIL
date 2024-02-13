"""
첫 줄에 마지막 노드번호 v, 간선 수 e
다음 줄에 e과 간선의 양 끝 노드 정보
인접 행렬로 표현된 재귀 dfs 활용
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def dfs(v):
    # 하고 싶은 일
    print(v, end=' ')
    # 방문체크
    visited[v] = 1
    # 시작정점(v)에 인접한 정점(w)중에
    for w in range(1,V+1):
        # 미방문한 정점이 있으면
        if adj_mat[v][w] == 1 and visited[w] ==0:
            # 재귀호출
            dfs(w)
V, E = map(int,input().split())               # 정점의 수, 간선 수 초기화
adj_mat = [[0] * (V + 1) for _ in range(V+1)] #인접 행렬 초기화
visited = [0] * (V+1)                         # 방분 체크 초기화
tmp = list(map(int,input().split()))

for i in range(E):
    s,e = tmp[2*i], tmp[2*i+1]
    adj_mat[s][e] = adj_mat[e][s] = 1 # 방향성 없음 (중요한 체크포인트)

dfs(1)