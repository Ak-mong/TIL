from heapq import heappop,heappush

INF = int(1e9) # 무한을 의미하는 값으면 10억
V, E = map(int,input().split())
start = 0 # 시작 노드 번호

# 인접 리스트
graph = [[] for _ in range(V)]
# 누적 거리를 저장할 변수 - INF 로 저장
distance = [INF] * V

# 간선 정보 저장
for _ in range(E):
    s, e, w = map(int,input().split())
    '''
    graph[3][4] = 34 # 인접 행렬 형식
    graph[3] = [[4,31]] # 인접 리스트 형식
    '''
    graph[s].append([e,w])

def dijkstra(start):
    pq = []
    # 시작 노드 최단 거리는 0
    # 시작점의 weight, node 번호를 한 번에 저장
    # heapq 에 리스트로 저장할 때는 맨 앞의 데이터를 기준으로 정렬된다.
    heappush(pq, (0, start))

    # 시작 노드 초기화
    distance[start] = 0

    # 우선순위 큐가 빌 때 까지 반복
    while pq:
        # 최단 거리 노드에 대한 정보 꺼내기
        dist, now = heappop(pq)

        # pq 의 특성 때문에 더 간거리가 미리 저장되어 있음
        # now 가 이미 더 짧은 거리로 온 적이 있다면 pass
        # == 현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue

        # now(현재 노드) 에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_node = to[0]
            next_dist = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist # 누적 거리르 최단 거리로 갱신
            heappush(pq, (new_dist, next_node)) # next_node의 인접 노드들을 추가
# 실행
dijkstra(start)
# print(distance)
# 모든 노드로 가기 위한 최단 거리 출력
for i in range(V):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INF", end=' ')
    else:
        print(distance[i], end=' ')