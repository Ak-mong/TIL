import sys;
sys.stdin = open('txt/maze.txt')
dr = [0,1,0,-1] # direction r
dc = [1,0,-1,0]
def mazeGo(N):
    global flag
    for i in range(N):
        for j in range(N):
            if maze_arr[i][j] == 2:
                r,c = i,j
    # print(r,c)
    # 이동경로
    stack = []
    # 방문확인
    visited = [[0] * N for _ in range(N)]
    # 시작점 표시
    stack.append((r,c))
    visited[r][c] = 1 # 출발점은 방문했기 때문
    # 시작점이 (0,0) 이 아니기 때문에 for문 사용할 필요가 없음
    while stack:# stack이 남아 있는동안만
        print(stack)
        # print(maze_arr)
        print(visited)

        cur_r,cur_c = stack[-1] # pop 하면 이 길이 아닐경우 다시 append해줘야되서
        #도착완료했으면 return 1
        if maze_arr[cur_r][cur_c] == 3:
            flag = 1
            return flag
        isok = 0 # 해당 위치에서 갈 곳이 없는지 확인
        # 4방향 체크
        for k in range(4):
            nr = cur_r + dr[k]
            nc = cur_c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and maze_arr[nr][nc] != 1: # 벽체크
                # 해야 되는 것
                if visited[nr][nc] != 1: # 방문한 곳이 아니라면
                    stack.append((nr,nc))
                    visited[nr][nc] = 1
                    isok = 1
                    break
        if not isok: # 갈 곳이 없으면?
            stack.pop()
    return flag
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    flag = 0 # 기본적으로 도착 못 한다.
    maze_arr = [list(map(int,input())) for _ in range(N)]
    # print(maze_arr)
    stack = []
    print(f'#{tc} {mazeGo(N)}')
