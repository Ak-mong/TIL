import sys;sys.stdin = open('txt/binary_search.txt')

def in_order(node):
    global value
    if node <= n:
        in_order(node*2) # 왼
        tree[node] = value
        value += 1
        in_order(node*2+1) # 오

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    bs = []
    tree = [0] * (n+1)
    value = 1
    in_order(1)

    print(f'#{tc} {tree[1]} {tree[n//2]}')
