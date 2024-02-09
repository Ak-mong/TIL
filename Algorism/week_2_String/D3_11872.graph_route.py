import sys;sys.stdin = open('txt/graph_route.txt')
def dfs(x, y): # 시작 x, 마지막 y
    # visited, stack 생성 및 초기화
    visited = [0] * (V+1)
    st = [] # 스택
    visited[x] = 1 # 시작점 방문
    while True: #탐색
        # 현재 방문한 정점에 인접하고 방문안한 정점 w가 있으면? (첫번째 조건)
        for w in adjl[x]:
            if visited[w] == 0: # 방문했으면 1이 되기때문에
                st.append(x) # push(x), x를 지나서
                x = w        # w에 방문
                visited[x] = 1 # 방문해서
                if x == y:
                    return 1
                break # for w
            elif visited[w] == 1 and not st: # 이미 한번 간곳인데 스택이 비어 있는데
                return 0
                break

        else: # for w, x에 남은 인접 정점이 없으면
            if st: # 스택이 비어있지 않으면 ( 지나온 정점이 남아 있으면)
                x = st.pop()
            else: # 스택이 비어있으면(출발점에서 남은 정점이 없으면?)
                # 탐색을 끝낸다
                if x != y: #탐색 끝냈는데 x가 y에 도달하지 못했다
                    return -1
                break # while True

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int,input().split())
    adjl = [[] for _ in range(V+1)] # 노드의 갯수가 1부터 존재하기 때문,
    for i in range(E):  # 간선에 대한 정보
        n1, n2 = arr[i][0], arr[i][1]  # 하나의 방식, 인접한 node1, node 2를 표현
        adjl[n1].append(n2)  # S -> G
    # print(arr)
    # print(S,G)
    # print(adjl)
    print(f'#{tc} {dfs(S,G)}')