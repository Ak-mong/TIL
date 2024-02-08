"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def dfs(x, V): # 시작 x, 마지막 V
    # visited, stack 생성 및 초기화
    visited = [0] * (V+1)
    st = [] # 스택
    visited[x] = 1 # 시작점 방문
    print(x) # 정점에서 할 일 # 방문한 정점 번호 출력
    while True: #탐색
        # 현재 방문한 정점에 인접하고 방문안한 정점 w가 있으면? (첫번째 조건)
        for w in adjl[x]:
            if visited[w] == 0: # 방문했으면 1이 되기때문에
                st.append(x) # push(x), x를 지나서
                x = w        # w에 방문
                visited[x] = 1 # 방문해서
                print(x)
                break # for w
        else: # for w, x에 남은 인접 정점이 없으면
            if st: # 스택이 비어있지 않으면 ( 지나온 정점이 남아 있으면)
                x = st.pop()
            else: # 스택이 비어있으면(출발점에서 남은 정점이 없으면?)
                # 탐색을 끝낸다
                break # while True

V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트
adjl = [[] for _ in range(V + 1)] # ardjl[i] 행에 i에 인접인 정점 번호
for i in range(E): # 간선에 대한 정보
    n1, n2 = arr[i*2], arr[i*2+1] # 하나의 방식, 인접한 node1, node 2를 표현
    adjl[n1].append(n2) # n1에도 n2에 연결
    adjl[n2].append(n1) # 방향이 없는 경우만 추가함, n2에도 n1을 추가한다.
dfs(1, V)
print(adjl) # 연결된것 확인할 수 있음
"""
[[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
0 에 인접한 건 없음
1에 인접한것은 2,3 등등
"""
