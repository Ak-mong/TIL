import sys; sys.stdin = open('txt/maze1.txt')

dr = [0,1,0,-1]
dc = [1,0,-1,0]
def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i,j
def find_goal(r,c):
    q = [(r,c)]
    visited[r][c] = 1 # 시작점 방문
    while q:
        r,c = q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 벽 체크
            if 0<= nr < N and 0<= nr < N and visited[nr][nc] == 0:
                if maze_arr[nr][nc] == 0: # 갈 수 있는 길이라면
                    q.append((nr,nc)) # 갈 수 있으면 더해라
                    visited[nr][nc] = visited[r][c] + 1
                if maze_arr[nr][nc] == 3: # 도착점에 도착한다면
                    return 1 # 가능
    return 0 # 갈 곳이 없네

T = 10
for _ in range(T):
    tc =int(input())
    N = 16
    maze_arr = [list(map(int,input())) for _ in range(N)]
    visited = [[0]* N for _ in range(N)]
    # print(f'#{tc}',maze_arr)
    end_r, end_c = find_start(maze_arr)
    print(f'#{tc} {find_goal(end_r, end_c)}')