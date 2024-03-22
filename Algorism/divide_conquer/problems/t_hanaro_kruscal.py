import sys;sys.stdin = open('hanaro.txt')
from heapq import heappop, heappush

def find_set(x):
    if parent[x] == x: return x
    else: return find_set(parent[x])

def kruskal(s):
    # 조합을 이용해서 간선의 배열
    idx = 0
    for i in range(n-1):
        for j in range(i+1,n):
            dist[idx][0] = i
            dist[idx][1] = j
            dist[idx][2] = (x_arr[i] - x_arr[j])**2 + (y_arr[i] - y_arr[j])**2
            idx += 1


    # 정렬
    dist.sort(key=lambda x:x[2])

    # 오름차순으로 간선을 가져와 사이클이 없으면 union
    for i in range(idx):
        x,y = dist[i][0], dist[i][1]
        px, py = find_set(x), find_set(y)
        edge_cnt = 0
        total = 0
        # union
        if px != py:
            parent[py] = px
            total = dist[i][2] * tax_rate
            edge_cnt += 1
        if edge_cnt == n -1 :continue


    return total
t= int(input())
for tc in range(1,t+1):
    n = int(input())
    x_arr = list(map(int,input().split()))
    y_arr = list(map(int,input().split()))
    tax_rate = float(input())

    # kruskal 변수들
    dist = [[0] * 3 for _ in range(n*(n-1)//2)]     # 섬들간의 거리
    parent = [i for i in range(n)] # make_set
    print(f'#{tc} {kruskal(0):.0f}')