# 인접 리스트 BFS
# 딕셔너리로 해볼 것
# 덱 써볼 것것
graph = [
    [1,3],
    [0,2,4],
    [1],
    [0,4],
    [1,3],
]

def bfs(start):
    visited = [0] * n # 재귀가 아니기 때문에 안에 있을 수 있음
    # 시작 노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        # 갈 수 있는 곳을 체크
        for to in graph[now]:
            if visited[to]: continue

            visited[to] = 1
            queue.append(to)

n = 5
bfs(0)

# visited = [0] * n  # 재귀를 사용한다면 밖에


