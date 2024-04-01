# 1991 트리 순회 실버 1
n = int(input())
dicts = {}
for i in range(n):
    node, p_l, p_r = map(str,input().split())
    dicts[node] =[p_l,p_r]
visited = [0] * (n+1)
def preorder(v):
    if v == '.':return
    print(v,end='')
    preorder(dicts.get(v)[0])
    preorder(dicts.get(v)[1])
preorder('A')
print()
def inorder(v):
    if v == '.':return
    inorder(dicts.get(v)[0])
    print(v,end='')
    inorder(dicts.get(v)[1])
inorder('A')
print()
def postorder(v):
    if v == '.':return
    postorder(dicts.get(v)[0])
    postorder(dicts.get(v)[1])
    print(v,end='')
postorder('A')
