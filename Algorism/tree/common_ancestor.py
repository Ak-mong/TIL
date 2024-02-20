import sys;sys.stdin = open('txt/common_ancestor.txt')
t = int(input())
def find_ancestor(n): # node번호를 받기
    # if tree[n][0] != tree[m][0]:
    #     find_ancestor(tree[n][0],tree[m][0])
    #     return n,m
    if tree[n][0]:
        find_ancestor(tree[n][0])
        return n
    return n


    # if n: # 노드 번호 = 노드 갯수
        # 현재 방식 root -> 왼 -> 오



for tc in range(1,t+1):
    V,E,node1,node2 = map(int,input().split())
    arr = list(map(int,input().split()))
    print(arr)
    tree = [[0,0,0] for _ in range(V+1)]
    for i in range(V-1):
        parent, child = arr[i*2],arr[i*2+1]
        # print(parent,child)
        tree[child][0] = parent # 자식의 0번째 인덱스는 부모
        if tree[parent][1] == 0:
            tree[parent][1] = child # 부모의 1번째 인덱스는 왼쪽 자식
        else:
            tree[parent][2] = child # 오른쪽 자식

        #     tree[parr]
    #     if left[parent] == 0:
    #         left[parent] = child
    #         tree[parent] = child
    #     else:
    #         right[parent] = child
    print(tree)
    # print(left)
    # print(right)
    print(find_ancestor(8))

    # print(tree_list)
    print('end')
    '''
    공통조상찾기
    읽는 방법에 대해서 구하는 것 X
    12 7 4 2 간의 순서를 고려할 수 있을까
    left[left[8]] = 8의 왼쪽 자식의 왼쪽 자식
    tree는 구현했다.
    if parent(8) == parent(13):
        8 하위 노드 갯수 구하기
     
    
    '''