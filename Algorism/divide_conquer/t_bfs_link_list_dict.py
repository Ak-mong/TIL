'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
from collections import deque

def bfs(v):
    # 인 큐 + 방문체크
    Q = deque()
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.popleft() # deque 할때 하고싶은일 하기
        print(v, end=' ')
        # 인접하고 미방문 -> 인큐
        for w in adj_lst[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1

V,E = map(int,input().split())
temp = list(map(int,input().split()))

adj_lst = {i:[] for i in range(1,V+1)} # 인접리스트 (딕셔너리)
# adj_lst = [[] for i in range(V+1)] # 인접 리스트 (리스트)
print(adj_lst)
visited = [0] * (V+1)

for i in range(E):
    s,e = temp[2*i], temp[2*i+1]

    adj_lst[s].append(e)
    adj_lst[e].append(s)

bfs(1)
print()
print(visited)