# 인접 행렬 DFS
graph = [
    [0,1,0,1,0], # 0 번 인덱스가 갈수있는 인덱스 저장
    [1,0,1,0,1], # 1 번 인덱스가 갈수있는 인덱스 저장
    [0,1,0,0,0], # 2 번 인덱스가 갈수있는 인덱스 저장
    [1,0,0,0,1], # 3 번 인덱스가 갈수있는 인덱스 저장
    [0,1,0,1,0], # 4 번 인덱스가 갈수있는 인덱스 저장
]

def dfs(now):
    # 기저 조건 : 현재 문제에는 없음

    # 다음 재귀함수 호출 전
    # visited[now] = 1
    # path.append(now)
    # print(now, end=' ')



    # 다음 재귀 호출
    # dfs : 현재 노드에서 다른 노드들을 확인
    # 다른 노드들 == 반복문
    for to in range(n):
        # 갈 수 없다면 pass
        if graph[now][to] == 0: continue

        # 이미 방문했다면 pass
        if visited[to]: continue

        visited[to] = 1
        path.append(to)

        dfs(to)
    # 돌아왔을 때 작업


n =5
# 무향 그래프니까
visited = [0] * n
path= []
# 출발점 초기화
visited[0] = 1
path.append(0)

dfs(0)
print(path)
