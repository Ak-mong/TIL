import sys
from collections import deque
sys.stdin =open('input.txt')
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

# 2716 원숭이 매달기 실버2
n = int(input())
for i in range(n):
    strings = input().strip()
    tree = []
    max_depth = 0
    for x in strings:
        if x == '[':
            tree.append(x)
        else:
            max_depth = max(max_depth, len(tree))
            tree.pop()
    print(2 ** max_depth)



# 5639 이진 검색 트리 골드 5
'''
완전 이진트리가 아닌데 이진검색을 함

'''
# path = []
# while True:
#     try:
#         a = int(input())
#         path.append(a)
#     except:
#         break
# print(path)
# visited = [False] * (len(path) + 1)
# new_path = []
# cnt = 1
# def tree(node):
#     global cnt
#     visited[0] = True
#     print(node, cnt)
#     for i in range(len(path)):
#         if node == path[i]: continue
#         if visited[i] : continue
#         if path[i] < node:
#             left = path[i]
#             new_path.append(left)
#             visited[i] = True
#             cnt += 1
#             tree(left)
#         elif path[i] > node:
#             right = path[i]
#             new_path.append(right)
#             visited[i] = True
#             cnt += 1
#             tree(right)
#         else:
#             pass
# tree(path[0])
#
# print(new_path)
#
# cnt2 = 1
# def back(level):
#     global cnt2
#     cnt2 += 1
#     back()
#     back(right)
#     print(node)


# import sys
#
# sys.setrecursionlimit(10 ** 9)
# nums = []
# while True:
#     try:
#         nums.append(int(sys.stdin.readline()))
#     except:
#         break
#
#
# def postorder(s, e):
#     if s > e:
#         return
#     mid = e + 1  # 오른쪽 노드가 없을 경우
#
#     for i in range(s + 1, e + 1):
#         if nums[s] < nums[i]:
#             mid = i
#             break
#
#     postorder(s + 1, mid - 1)  # 왼쪽 확인
#     postorder(mid, e)  # 오른쪽 확인
#     print(nums[s])
#
#
# postorder(0, len(nums) - 1)
#
# dict = {}







# 20364 부동산 다툼 실버1
# 이진트리

# def maketree(node):
#     if node >n: return
#     tree[node][0] = node // 2
#     tree[node][1] = node * 2
#     tree[node][2] = node * 2 + 1
#     maketree(node * 2) # 왼쪽
#     maketree(node * 2 + 1) # 오른쪽
#     # path.append(node)
#
# def goland(node,goal):
#     global flag,result
#     if flag: return
#     if node > n:return
#     path.append(node)
#     if saves[node] and node <= goal // 2 :
#         flag = 1
#         result = node
#         return
#     if node == goal:
#         flag = 1
#         saves[node] = 1
#         return
#     goland(node*2,goal)
#     goland(node*2+1,goal)
#
# n,q = map(int,input().split())
# arr = []
# tree = [[0] * 3 for _ in range(n+1)] # parent = 0, left = 1, right = 2
# visited = [0] * (n+1)
# saves = [0] * (n+1)
# maketree(1)
# print(tree)
# for i in range(1,q+1):
#     # arr.append((i,int(input())))
#     result = 0
#     path = []
#     flag = 0
#     land = int(input())
#     # maketree(1)
#     goland(1,land)
#     # print(i,visited)
#     # print(i,tree)
#     print(path)
#     print(result)


# dfs(1)
# print(tree)
# for i in range(q):
#     sors, land = map(arr[i])
# def maketreesssssssssssssssss(node):
#     global result, flag
#     if flag:
#         return
#     if node > n:
#         return
#     if saves[node]:
#         flag = 1
#         result = node
#         return
#     if node == land and not saves[node]:
#         visited[node] = 1
#         saves[node] = 1
#         flag = 1
#         result = 0
#         return
#     parent = node // 2
#     leftchild = node * 2
#     rightchild = node * 2 + 1
#     tree[node][0] = parent
#     tree[node][1] = leftchild
#     tree[node][2] = rightchild
#     maketree(leftchild)
#     maketree(rightchild)
# def golandssssssssss(node):
#     global result
#     deq = deque()
#     deq.append(node)
#     while deq:
#         value = deq.popleft()
#         if visited[value]: continue
#         if value == land:
#             visited[value] = 1
#             return
#         for child in tree[value][1:]:
#             if child > n: continue
#             if child == land:
#                 # 이 부분 고치기
#                 visited[child] = 1
#                 result = 0
#                 return
#             ###################
#             deq.append(child)