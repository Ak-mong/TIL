import sys;sys.stdin = open('../txt/subtree.txt')
def preorder(node):
    global cnt
    if node:
        cnt += 1
        preorder((tree[node][0]))
        preorder((tree[node][1]))
t = int(input())
for tc in range(1,t+1):
    cnt = 0
    e, n = map(int,input().split())
    v = e+1
    tree= [[0]*3 for _ in range(v+1)]
    tmp = list(map(int,input().split()))
    for i in range(e):
        p,c = tmp[i*2], tmp[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p
    preorder(n)
    print(f'#{tc} {cnt}')