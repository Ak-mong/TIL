import sys;sys.stdin = open('../txt/common_ancestor.txt')

def search_ancestor(n):
    p = tree[n][2]  # 부모노드
    ancestor = []   # 조상들
    while p != 0: # root 가 아닌동안
        ancestor.append(p) # 일단 넣고 시작
        p = tree[p][2]
    return ancestor

def common_ancestor(p1,p2):
    for i in range(len(p1)):
        for j in range(len(p2)):
            if p1[i] == p2[j]:
                return p1[i]
def preorder(node):
    global cnt
    if node:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

t = int(input())
for tc in range(1,t+1):
    V, E, n1, n2 = map(int, input().split())
    tree = [[0]*3 for _ in range(V + 1)]
    tmp = list(map(int,input().split()))
    for i in range(E):
        p, c = tmp[i*2], tmp[i*2+1]
        if tree[p][0] ==0:
            tree[p][0] =c
        else:
            tree[p][1] = c
        tree[c][2] = p

    p1 = search_ancestor(n1)
    p2 = search_ancestor(n2)
    CA = common_ancestor(p1,p2)
    cnt = 0
    preorder(CA)
    print(f'#{tc} {CA} {cnt}')