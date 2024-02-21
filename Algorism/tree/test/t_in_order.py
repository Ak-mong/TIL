import sys; sys.stdin = open('../txt/in_order.txt')

def inorder(node):
    if node <= n:
        inorder(2*node)
        ans.append(tree[node])
        inorder(2*node+1)
t = 10
for tc in range(1,t+1):
    n = int(input())
    tree = [''] * (n+1)
    for i in range(n):
        tmp = list(map(str,input().split()))
        idx = int(tmp[0])
        tree[idx] = tmp[1]
    # print(tree)
    ans = []
    inorder(1)
    print('f#{tc}', ''.join(ans))