import sys;sys.stdin = open('input.txt')
'''
서울(0), 천안(1), 원주(2), 논산(3), 대전(4),
대구(5), 강릉(6), 광주(7), 부산(8), 포항(9)
'''
'''
9 14
0 1 12
0 2 15
1 3 4
1 4 10
2 5 7
2 6 21
3 4 3
3 7 13
4 5 10
5 8 9
5 9 19
6 9 25
7 8 15
8 9 5
'''
# 힙 사용없는 우선순위 큐
# visited 와 최소값만 구할 줄 알면 된다.
def prim(s):
    # 출발점 설정
    D[s] = 0
    total = 0
    for _ in range(V+1): # 모든 도시를 선택
        # 가중치 최소 값 찾기
        min_v = INF
        for i in range(V+1):
            if visited[i] == 0 and min_v > D[i]:
                min_v = D[i]
                v = i

        # 방문 처리
        visited[v] = 1 # 다음번에 찾을 때 다시 안 구하기 위해서
        total += adj[PI[v]][v] # total += adj[부모][현재]

        # 인접도시 업데이트
        for w in range(V+1):
            if adj[v][w] and not visited[w]:
                if D[w] > adj[v][w]:
                    D[w] = adj[v][w]
                    PI[w] = v
    return total

V, E = map(int,input().split())
adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
INF = int(1e9)
D = [INF] *(V+1)                # 가중치
PI = [i for i in range(V+1)]    # 부모
visited = [0] * (V+1)           # 방문

for i in range(E):
    s, e, w = map(int,input().split()) # 시작 , 끝,  가중치
    adj[s][e] = adj[e][s] = w          # 무향 그래프라서
print(prim(0))
