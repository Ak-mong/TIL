import sys
from collections import deque
sys.stdin =open('input.txt')
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

# 20364 부동산 다툼 실버1
# 이진트리
def maketree(node):
    if node > n:
        return
    parent = node // 2
    leftchild = node * 2
    rightchild = node * 2 + 1
    tree[node][0] = parent
    tree[node][1] = leftchild
    tree[node][2] = rightchild
    maketree(leftchild)
    maketree(rightchild)
def goland(node):
    global result
    deq = deque()
    deq.append(node)
    while deq:
        value = deq.popleft()
        # if value == land:
        #     visited[value] = 1
        #     return
        for child in tree[value][1:]:
            if child > n: continue
            if child == land:
                # 이 부분 고치기
                result = value
                return
                visited[child] = 1
                result = 0
                return
            ###################
            deq.append(child)

n,q = map(int,input().split())
arr = []
tree = [[0] * 3 for _ in range(n+1)]
# parent = 0, left = 1, right = 2
visited = [0] * (n+1)
result = 0
maketree(1)
for i in range(1,q+1):
    # arr.append((i,int(input())))
    land = int(input())
    goland(1)
    # print(i,visited)
    # print(i,tree)
    print(result)


# dfs(1)
# print(tree)
# for i in range(q):
#     sors, land = map(arr[i])
