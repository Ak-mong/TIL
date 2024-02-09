import sys; sys.stdin = open('txt/input.txt')
for _ in range(1,11):
    t, n = map(int,input().split())
    # 순서 쌍
    arr = list(map(int, input().split()))
    # 갈 수 있는 도시 찾기
    adj = [[0] * 100 for _ in range(2)]
    for i in range(n):
        # 첫 번째 길이라면?
        if adj[0][arr[i*2]] == 0:
            adj[0][arr[i*2]] = arr[i*2+1]
        # 두 번째 길이라면?
        else:
            adj[1][arr[i * 2]] = arr[i * 2 + 1]

    # 방문 여부
    visited = [0]* 100
    visited[0] = 1
    #가는 경로
    stack=[0] # while문에 넣기 위해 넣어둠
    result = 0 # result 초기화 및 탐색 실패시 출력되게 됨

    while stack: #스택이 존재하는 동안
        top = stack[-1] # 스택의 가장 위에 쌓인 것
        # 도착했니?
        if top == 99:
            result = 1 # 도착했네
            break # while 나가기
        for i in range(2): #0, 1 둘 중 하나
            # 길이 있고, 방문한 적이 없다?
            if adj[i][top] != 0 and not visited[adj[i][top]]:
                stack.append(adj[i][top]) # 스택에 추가
                visited[adj[i][top]] = 1 # 방문했다에 추가
                break # for i
            # 길이 없다면? 돌아가라
        else:
            stack.pop()
    print(f'{t} {result}')