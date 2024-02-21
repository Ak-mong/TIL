import sys;sys.stdin = open('txt/node_len.txt')

def solutions(node): # 트리의 인덱스 번호를 활용하는 것
    if node > n: # 노드가 최대 값을 넘어버리면
        return 0 # 예외처리

    # 후위 순회
    if tree[node] == 0 : # 해당노드의 부모가 없다면?
        tree[node] = solutions(node*2) + solutions(node*2+1)

    # 부모에서 부터 내려오기 때문에 0 + 0 = 0 이 되서 무한 반복함
    # while not tree[node]: # 부모자식이 없다면
    #     tree[node] = tree[node*2] + tree[node*2+1]
    return tree[node] # 재귀를 위한 return

t = int(input())
for tc in range(1,t+1):
    n,m,L = map(int,input().split())  # 노드의 갯수 5, 리프노드의 개수 3, 값을 출력할 노드 번호 2
    tree = [0]* (n+1) # 트리 선언
    # arr = [list(map(int,input().split())) for _ in range(m)] # 인덱스-값
    for i in range(m):
        node, value = map(int,input().split())
        tree[node] = value
    solutions(1) # 루트는 항상 1이라서
    print(f'#{tc} {tree[L]}')

