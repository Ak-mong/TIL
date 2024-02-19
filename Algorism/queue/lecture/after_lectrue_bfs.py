
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
 인접 행렬로 저장하기 : 노드 번호를 인덱스로 활용
'''
V, E = map(int,input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
data = list(map(int,input().split()))
for i in range(0,E * 2, 2):
    # 1번 노드와 2번 노드가 연결되어있으면
    # adj[1][2] = 1
    # adj[2][1] = 1
    adj[data[i]][data[i+1]] = 1
    adj[data[i+1]][data[i]] = 1
for row in adj:print(row)

# 이제 그래프 제대로 입력 받았으니 ... BFS 탐색 수행
# 현재 위치에서 갈 수 있는 경로를 모조리 저장해뒀다가
# 발견 순서대로 방문 : BFS
# 순서대로? Queu를 활용하면 되겠다!!
# queue를 위한 방법입니다 라고 한다면 목적과 수단이 바뀐것
def bfs(start):
    queue = [start]  # 리스트지만 큐처럼 활용
    # 0 : 미방문, 1: 방문한 노드
    visited = [0] * (V + 1)  # 재 방문을 막기 위해 방문 여부 표시
    visited[start] = 1
    while queue: # 발견한 경로를 순서대로 방문
        current = queue.pop(0)
        # 현재 노드에서 방문할 수 있는 노드 탐색
        # 방문할 수 있는 노드? : 인접하면서, 방문하지 않은 노드
        # adj[current]  #  current와 연결되어 있는 노드 정보
        print(current, end=' ')
        # 히ㅕㄴ재 노드와 연결되어 있는지 확인!
        for i in range(V+1):
            # adj[current][i] == 1 이면 나랑 연결됨
            # visited[i] == 0 이면 미방문
            if adj[current][i] and not visited[i]:
                queue.append(i) # i 번 노드에 갈 수 있다.
                visited[i] = 1 # 방문했다, 반복을 줄이기 위해 여기 넣었음
        # 전부 방문 확인
bfs(1)



