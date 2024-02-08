import sys;sys.stdin = open('txt/graph_route.txt')
T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    adjl = [[] for _ in range(V+1)] # 노드의 갯수가 1부터 존재하기 때문,
    for i in range(E):  # 간선에 대한 정보
        S, G = arr[i], arr[i+ 1]  # 하나의 방식, 인접한 node1, node 2를 표현
        adjl[S].append(G)  # S -> G