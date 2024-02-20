import sys;sys.stdin = open('txt/subtree.txt')
def calc_node(start_node):
    global node_cnt
    if tree[start_node][1]:
        node_cnt += 1 # 왼쪽 자식노드가 있을 떄 하나 추가
        calc_node(tree[start_node][1]) # w자식노드로 가서 재귀
    if tree[start_node][2]:
        node_cnt += 1 #오른쪽 자식노드가 있을 때 하나 추가
        calc_node(tree[start_node][2]) # w자식노드로 가서 재귀

t= int(input())
for tc in range(1,t+1):
    E, N = map(int,input().split())
    V = E + 1
    adjl = list(map(int,input().split()))
    tree = [[0] *3 for _ in range(V+1)]
    for i in range(E):
        parent, child = adjl[i*2], adjl[i*2+1]
        tree[child][0] = parent # 0 에 부모
        if tree[parent][1]:
            tree[parent][2] = child
        else:
            tree[parent][1] = child
    node_cnt = 1
    calc_node(N)
    print(f'#{tc} {node_cnt}')
