import sys
from collections import deque
sys.stdin =open('input.txt')
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# 1931 회의실 배정 실버 1
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x : x[1])
print(arr)
s = arr[0][0]
e = arr[len(arr)-1][1]
print(s,e)
index = 0
while s < e:
     s = arr[index][1]







# # 4803  트리 골드 4
# n,m= map(int,input().split())
# # n 정점의 개수, m 간선의 개수
# adjl = [[] for _ in range(n+1)]
# for i in range(m):
#     s,e = map(int,input().split())
#     adjl[s].append(e)
#     adjl[e].append(s)
#
# print(adjl)
# path = []
# visited = [0] * (n+1)
# visited[1] = 1
# def dfs(level):
#     if len(path) == n:
#         print(path)
#     for i in adjl[level]:
#         if visited[i]: continue
#         path.append(i)
#         dfs(i)
#         path.pop()
#
#
# dfs(1)