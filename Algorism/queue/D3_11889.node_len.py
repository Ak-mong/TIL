import sys;sys.stdin = open('txt/node_len.txt')
def node_len(s,g):
    q = []
    visited = [0] * (V + 1)
    # 시작점을 큐에 넣고 방문체크
    visited[s] = 1
    q.append(s)
    while q:
        r = q.pop(0)
        # 하고픈 일
        if r == g: # 뽑아낸곳이 골인 지점이라면?
            return visited[r]-1
        for w in adjl[r]: # 정점 r에서 갈 수 있는 루트
            if not visited[w]: # 방문하지 않았다면
                q.append(w)     #큐에 정점을 넣어놔라
                visited[w] = visited[r] + 1 # 시작점포함 몇개정점째인지
    return 0 # 못갈경우 0 출력

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1,n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    s,g = map(int,input().split())
    # print('#',tc)
    # print(s,g)
    # print(adjl)
    print(f'#{tc} {node_len(s,g)}')
    # print()