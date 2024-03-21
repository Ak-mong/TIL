# import sys;sys.stdin=open('input.txt',"r")
from heapq import heappush,heappop # 우선순위 큐라서 사용해야 한다.
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

def prim(start):
    # priorityque
    pq = []
    MST = [0] * V # visited 역할

    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    '''
    [기존 BFS] 노드 번호만 관리
    [Prim] 가중치가 낮으면 먼저 나와야 한다.
    -> 관리해야할 데이터 : 가중치, 노드 번호
    -> 동시에 두가지 데이터 다루기
        1. class 로 만들기
        2. 튜플로 관리
    이차원배열 + 가중치 + 높이 라면? 튜플로 관리하기 어렵다.
    => 3가지 이상은 클래스로 해야한다.
    '''
    heappush(pq, (0,start))

    while pq:
        weight, now = heappop(pq)
        '''
        # 우선순위 큐의 특성 상,
        # 더 먼거리로 가는 아법이 큐에 저장이 되어 있기 때문에
        # 기존에 이미 더 짧은 거리로 방문했다면, continue
        '''
        # 방문 했다면 continue
        if MST[now]:
            continue
        # 방문 처리
        MST[now] = 1
        # 누적 합 추가
        sum_weight += weight
        print(weight, end=' ')
        # 갈수 있는 노드들을 보면서
        for to in range(V):
            if graph[now][to] == 0 or MST[to]: # 합친것
               continue

            '''
            # 갈 수 없다면 pass
            if graph[now][to] == 0:
                continue
            # 이미 방문했다면 pass
            if MST[to]:
                continue
            '''
            heappush(pq, (graph[now][to],to))

    print(f'최소비용 : {sum_weight}')
V, E = map(int,input().split())
# 인접 행렬로 저장
# - [실슴] 인접 리스트로 저장
graph = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    s,e,w = map(int,input().split())
    # 가중치 저장
    '''
    # [기존] 3~4 로 갈 수 있다.
    graph[3][4] = 1

    # [가중치 그래프] 3-> 4 로 가는데 31이라는 비용이 든다.
    graph[3][4] = 31
    '''
    graph[s][e] = w
    graph[e][s] = w  # 무방향 그래프
# print(graph)
prim(0)
'''
BFS : 무조건 방문
PRIM : 일단 pq에 넣고 방문 X
'''