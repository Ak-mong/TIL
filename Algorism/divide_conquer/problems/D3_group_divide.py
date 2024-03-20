import sys;sys.stdin = open('group_divide.txt')

def find(x):
    # 기저 조건
    # 재귀함수 호출 전
    # 재귀함수 호출
    for to in adj_lst[x]:
        if visited[to]: continue
        visited[to] = True
        find(to)

t = int(input())
for tc in range(1,t+1):
    V,E = map(int,input().split())
    arr = list(map(int,input().split()))
    adj_lst = {x:[] for x in range(1,V+1)}
    for i in range(0,E): # 무향 그래프
        adj_lst[arr[2*i]].append(arr[2*i+1])
        adj_lst[arr[2*i+1]].append(arr[2*i])
    # print(adj_lst)
    visited = [False] * (V+1)
    cnt = 0
    for x in range(1,V+1):
        if visited[x]: continue
        cnt += 1
        find(x)
    print(f'#{tc} {cnt}')