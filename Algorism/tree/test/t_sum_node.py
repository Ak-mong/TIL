'''
post(node)
if node <= N:
    # 잎노드
    if tree[node]:
        return tree[node]
    # 가지노드
    else:
        # post_order
        l = post(node * 2)
        r = post(node * 2 + 1)
        tree[node] = 1 + r
        return tree[node]

'''
import sys;sys.stdin = open('../txt/node_len.txt')

def postorder(node):
    if node <= N:
        # 잎노드
        if tree[node]:
            return tree[node]
        # 가지노드
        else:
            l = postorder(2 * node)
            r = postorder(2 * node + 1)
            tree[node] = l + r
            return tree[node]
    else:
        return 0

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())  # 노드수, 리프노드수, 출력노드
    tree = [0] * (N + 1)  # 완전이진트리
    for i in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    # print(tree)
    postorder(1)
    print(f'#{tc} {tree[L]}')