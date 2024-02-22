import sys; sys.stdin = open('../txt/binary_search.txt')
def inorder(node): # node 트리의 인덱스 번호
    global num
    if node <= n:
        inorder(2 * node)
        # 할일
        tree[node] = num
        num += 1
        inorder(2 * node+1)

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    tree = [0]  * (n+1) # 완전 이진 트리
    num = 1 # 왜 이걸 달아놔야 될까.... 노드의 값
    inorder(1)
    print(f'#{tc} {tree[1]}  {tree[n//2]}')