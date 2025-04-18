import sys;sys.stdin = open('../txt/4calc.txt')
# V번 연산의 결과를 반환하는 함수 >> 후위연산
def solve(v):
    # 만약 v번 노드에 value가 숫자라면 그냥 반환
    # 연산자라면 계산해서 반환
    # 연산을 해야되기 때문에 후위순회 해야 한다
    if tree[v][2] not in '+*-/': # 숫자라면?
        return int(tree[v][2])

    result1 = solve(tree[v][0]) # v번 노드의 왼쪽자식의 결과
    result2 = solve(tree[v][1]) # v번 노드의 오른쪽자식의 결과
    if tree[v][2] == '+':
        return result1 + result2
    elif tree[v][2] == '*':
        return result1 * result2
    elif tree[v][2] == '-':
        return result1 - result2
    else:
        return result1 /result2

    pass
# 노드 value 각 노드가 어떤 value를 가지는지 저장
# 노드 간의 연결 정보도 표시 해야함
for tc in range(1,11):
    N = int(input()) # 정점의 개수
    # 3개 짜리 트리를 만들자
    #왼쪽, 오른쪽, value 저장
    # => [0]*3
    # 0 : 왼쪽 자식, 1: 오른쪽 자식, 2: 노드가 가진 값
    tree = [[0]*3 for _ in range(N+1)]
    for _ in range(N):
        # 노드 정보
        node = input().split()
        # 0 노드 번호, 1: value. 2: 왼쪽자식 3: 오른쪽 자식
        if len(node) == 2: # 단말 노드(잎 노드)이다. value = 숫자다
            v = int(node[0])
            value = node[1] # 문자열 형태 숫자
            tree[v][2] = value
        else:
            v = int(node[0])
            value = node[1] # 연산자
            left = int(node[2])
            right = int(node[3])
            tree[v][2] = value
            tree[v][0] = left
            tree[v][1] = right
    result = int(solve(1))
    print(f'#{tc} {result}')
    # for row in tree:
    #     print(row)
    # print()