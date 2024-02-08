"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
# 재귀에 저장하는 방법
def dfs2(x): # 시작 x, 마지막 V
    visited[x] = 1 #방문표시
    print(x)   # 출력
    # x에 인접하고 방문안한 w가 있으면
    for w in adjl[x]:
        if visited[w] == 0:
            dfs2(w)

V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트
adjl = [[] for _ in range(V + 1)] # ardjl[i] 행에 i에 인접인 정점 번호
for i in range(E): # 간선에 대한 정보
    n1, n2 = arr[i*2], arr[i*2+1] # 하나의 방식, 인접한 node1, node 2를 표현
    adjl[n1].append(n2) # n1에도 n2에 연결
    adjl[n2].append(n1) # 방향이 없는 경우만 추가함, n2에도 n1을 추가한다.

visited = [0] * (V+1) #
dfs2(1)
# print(adjl) # 연결된것 확인할 수 있음
"""
[[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
0 에 인접한 건 없음
1에 인접한것은 2,3 등등
"""
