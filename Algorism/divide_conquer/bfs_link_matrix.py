# 인접 행렬 BFS
'''
# 1. 갈 수 있는 곳 다가기
# 2. 방문 순서대로 다음 노드
먼저 방문 -> 먼저 다음 노드 : 큐
'''
graph = [
    [0,1,0,1,0], # 0 번 인덱스가 갈수있는 인덱스 저장
    [1,0,1,0,1], # 1 번 인덱스가 갈수있는 인덱스 저장
    [0,1,0,0,0], # 2 번 인덱스가 갈수있는 인덱스 저장
    [1,0,0,0,1], # 3 번 인덱스가 갈수있는 인덱스 저장
    [0,1,0,1,0], # 4 번 인덱스가 갈수있는 인덱스 저장
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
        for to in range(n):
            if graph[now][to] == 0: continue
            if visited[to]: continue

            visited[to] = 1
            print(visited) # 디버깅용
            queue.append(to)


n = 5
bfs(0)

# visited = [0] * n  # 재귀를 사용한다면 밖에


