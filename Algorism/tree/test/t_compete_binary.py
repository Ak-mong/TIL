'''
8                // 첫 번째 케이스의 N
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''


def in_order(node):
    if node <= N:
        in_order(2*node) # 왼쪽 자식
        print(tree[node], end='') # 루트
        in_order(2*node+1) # 오른쪽 자식

tree = ['','W', 'F', 'R', 'O', 'T', 'A', 'E', 'S'] # 완전이진트리
N = 8
in_order(1)