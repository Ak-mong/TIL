# v번 노드 요소 출력, in_order
def in_order(v):
    # v가 존재하지 않는 노드라면 재귀호출 멈춰!
    if v > N:
        return
    in_order(v*2)
    # v번의 왼쪽 서브트리 부터 처리
    print(tree[v],end='')
    # v번의 오른쪽 서브트리 처리
    in_order(v*2+1)


T = 10
for tc in range(1,T+1):
    # 총 노드의 개수
    N = int(input())
    # 완전이진트리에...
    # 중간에 비어있는 노드 번호가 없기 때문에
    # 배열에 저장가능
    tree = [None]*(N+1)
    for _ in range(N):
        node = input().split()
        #네 개 또는 두 개 짜리 요소 인데.. .
        # 트리를 그리기 위해서는 사실은 앞에 2개만 알면 됩니다.
        # node[0]: 노드 번호,  node[1] : 값
        tree[int(node[0])] = node[1]
    # print(tree)
    in_order(1)


'''
8               
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''