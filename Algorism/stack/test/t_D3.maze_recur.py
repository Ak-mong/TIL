import sys;sys.stdin = open('../txt/maze.txt')
# 2를 찾았다
# 상하좌우로 움직인다 + 방문체크
dr = [0,1,0,-1] # direction r
dc = [1,0,-1,0]
# 못만났다면 되돌아간다
# 3을 만났으면 출발점으로 되돌아와서 stack을 비운다. DFS
def dfs(r,c): # 4,3
    global flag
    if maze_arr[r][c] == 3:
        flag = 1
        return
    # 방문체크
    maze_arr[r][c] = 9 # 9에 큰 의미 는 없음
    # 인접한 정점, 미방문 -> 재귀
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        # index, 벽, 방문 체크
        if 0 <= nr < N and 0 <= nc < N and (maze_arr[nr][nc] == 0 or maze_arr[nr][nc] == 3):
            dfs(nr,nc)
def find_rc(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r,c = i, j
                return r,c
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    flag = 0 # 기본적으로 도착 못 한다.
    maze_arr = [list(map(int,input())) for _ in range(N)]
    sr, sc = find_rc(maze_arr)
    dfs(sr, sc)
    print(f'#{tc} {flag}')
