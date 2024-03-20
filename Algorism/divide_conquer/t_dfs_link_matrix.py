'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    # 인접 정점, 미 방문한 정점을 다시 재귀호출
    for w in range(1, V+1):
        if adj_mat[v][w] == 1 and visited[w] ==0:
            dfs(w)


V,E = map(int,input().split())
temp = list(map(int,input().split()))

adj_mat = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
visited= [0] * (V+1)

for i in range(E):
    s,e = temp[2*i],temp[2*i+1]
    adj_mat[s][e] = adj_mat[e][s] = 1
dfs(1)