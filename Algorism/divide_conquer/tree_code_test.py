arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

# 코딩 테스트에서는 간단하게
nodes = [[] for _ in range(14)]
for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].append(child_node)


# 자식이 없다는 걸 표시하기 위해 None
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)
print(nodes)

# 중위순회 구현
def inorder(nodeNum):
    # 갈 수 없다면 skip
    if nodeNum == None:
        return
    #dhlsWHr 왼쪽으로 갈 수 있다면 진행
    inorder(nodes[nodeNum][0])
    print(nodeNum, end=' ')
    # 오른쪽으로 갈 수 있다면 진행
    inorder(nodes[nodeNum][1])