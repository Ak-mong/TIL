# 인접 리스트 DFS
graph = [
    [1,3],
    [0,2,4],
    [1],
    [0,4],
    [1,3],
]

def dfs(now):
    # 기저 조건 : 현재 문제에는 없음

    # 다음 재귀함수 호출 전
    # visited[now] = 1
    # path.append(now)

    # 다음 재귀 호출
    # 인접 리스트
    # 차이점1. 갈 수 없는 곳 조건 필요없음
    # 차이점2 . for문 작성 시 인덱스 사용 필요없다.
    for to in graph[now]:
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
