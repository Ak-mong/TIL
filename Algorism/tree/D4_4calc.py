import sys;sys.stdin = open('txt/4calc.txt')

def solve(node):
    if node > n:
        return 0
    if tree[node][2] not in '+-*/': # 연산자라면
        return int(tree[node][2]) # 정수 값으로 return한다

    result1 = solve(tree[node][0]) # 왼쪽 자식 노드
    result2 = solve(tree[node][1]) # 오른쪽 자식 노드
    if tree[node][2] == '*':
        return result1 * result2
    elif tree[node][2] == '/':
        return result1 / result2
    elif tree[node][2] == '+':
        return result1 + result2
    else:
        return result1 - result2
    return tree[node][2]


for tc in range(1,11):
    n = int(input())
    # 0: 노드번호, 1: value, 2: 왼쪽자식 3: 오른쪽 자식
    tree = [[0]*3 for _ in range(n+1)]

    # 트리 만들기
    for _ in range(n):
        node = input().split() # 문자열로 된 리스트
        # 0: 노드번호, 1: value, 2: 왼쪽자식 3: 오른쪽 자식
        if len(node) == 2:  # 단말 이다, value가 숫자
            tree[int(node[0])][2] = node[1]  # 문자열 형태 숫자
        else:
            tree[int(node[0])][2] = node[1]
            tree[int(node[0])][0] = int(node[2])
            tree[int(node[0])][1] = int(node[3])
        # print(tree)

    # 루트정점의 번호는 1이다.
    result = int(solve(1))
    print(f'#{tc} {result}')
