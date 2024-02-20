'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(node):
    if node != 0:
        print(node, end=' ')
        pre_order(tree[node][0])
        pre_order(tree[node][1])
V = int(input()) # 정점
E = V-1 # 간선
tree = [[0]*3 for _ in range(V+1)] # 인접리스트
tmp = list(map(int, input().split()))
for i in range(E):
    parent, child = tmp[2*i], tmp[2*i+1]
    if not tree[parent][0]: # 왼쪽자식이 없다면
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    tree[child][2] = parent
print()

# root 찾기
c = V
while tree[c][2] != 0:
    child = tree[c][2]
root = c
print()

pre_order(root)