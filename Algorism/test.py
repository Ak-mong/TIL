import sys;sys.stdin =open('input.txt')
def inorder(node):
    if node <= n:
        inorder(2*node)
        ans.append(tmp[node])
        inorder(2*node+1)
t = int(input())
for tc in range(1,t+1):
    e, n = map(int,input().split())
    arr = list(map(int,input().split()))
    tree = [''] * (n+1)
    num = 1
    ans = []
    inorder(1)
    print(ans)