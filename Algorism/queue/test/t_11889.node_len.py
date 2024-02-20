import sys;sys.stdin = open('../txt/node_len.txt')
T = int(input())
def bfs(v):
    # enQ
    # 인접하고 미방문 + 방문체크
    Q = [v]
    visited[v] = 1
    while Q:
        #v = deQ
        v = Q.pop(0)
        if v ==goal:
            return visited[v] -1
        #인접하고 미방문(w)
        for w in adj_lst[v]:
            if visited[w] ==0:
                Q.append(w)
                visited[w] = visited[v] + 1
    return 0 #경로가 없는 경우
for tc in range(1,T+1):
    V, E = map(int,input().split())
    adj_lst = [[] for _ in range(V+1)] # 인접리스트
    visited = [0] * (V+1)
    # 인접리스트에 저장
    for i in range(E):
        s, e = map(int,input().split())
        adj_lst[s].append(e)
        adj_lst[e].append(s)
    start, goal = map(int,input().split())
    print(f'#{tc} {bfs([start])}')

