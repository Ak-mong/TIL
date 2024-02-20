import sys;sys.stdin = open('txt/common_ancestor.txt')
t = int(input())
def find_parents(n,parent_arr): # node번호를 받기
    # if tree[n][0] != tree[m][0]:
    if tree[n][0]:
        parent_arr.append(tree[n][0]) # 부모를 더해간다.
        find_parents(tree[n][0],parent_arr)

# 현재 방식 root -> 왼 -> 오
def find_ancestor(parent1, parent2):
    for p1 in parent1:
        for p2 in parent2:
            if p1 == p2:  # 하나씩 비교하다가 같은것이 있을 때
                return p1
def calc_degree(node):
    global ancestor_size # 증가시킬것이기 때문
    for x in range(1,3): #이진 트리니까, 그리고 자식노드가 1, 2에 저장했기 때문에
        if tree[node][x]: # 해당 node에 자식노드가 있다면
            ancestor_size += 1 # 차수를 늘리겠다.
            calc_degree(tree[node][x]) # 그리고 자식 노드로 가서 다시 탐사하겠다.


for tc in range(1,t+1):
    V,E,node1,node2 = map(int,input().split())
    adjl = list(map(int,input().split()))

    tree = [[0,0,0] for _ in range(V+1)]
    for i in range(V-1):
        parent, child = adjl[i*2],adjl[i*2+1]
        tree[child][0] = parent # 자식의 0번째 인덱스는 부모
        if tree[parent][1] == 0:
            tree[parent][1] = child # 부모의 1번째 인덱스는 왼쪽 자식
        else:
            tree[parent][2] = child # 오른쪽 자식
    # 각 부모 노드
    node1_arr = []
    node2_arr = []
    find_parents(node1,node1_arr) # node1_arr 채우기
    find_parents(node2,node2_arr) # node2_arr 채우기
    # 조상 노드 찾기
    common_ancestor = find_ancestor(node1_arr,node2_arr) # 두 개의 리스트를 비교해서 리턴
    ancestor_size = 1 # 기본적으로 자기자신 노드를 포함하기 때문
    calc_degree(common_ancestor) # 조상님 노드부터 숫자 세기
    print(f'#{tc} {common_ancestor} {ancestor_size}')