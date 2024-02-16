import sys;sys.stdin = open('txt/maze_len.txt')
dr = [0,1,0,-1]
dc = [1,0,-1,0]

def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] ==2:
                r,c = i,j
                return r,c # local
def maze_go(r,c):
    global flag
    q = [(r,c)]
    visited[r][c] = 1
    while q:
        r,c = q.pop(0)
        for k in range(4):
            nr = r + dr[k] # 4방향으로 갈 행
            nc = c + dc[k] # 4방향으로 갈 열
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if maze_arr[nr][nc] == 0:
                    maze_arr[nr][nc] = 9 # 방문했다
                    q.append((nr,nc))
                    visited[nr][nc] = visited[r][c] + 1
                if maze_arr[nr][nc] == 3:
                    return visited[r][c]-1
    return 0
T = int(input())
for tc in range(1,T+1):
    N = int(input()) # N 미로의 한 변 크기
    maze_arr = [list(map(int,input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    r, c = find_start(maze_arr) # global
    # print(r,c)
    print(f'#{tc} {maze_go(r,c)}')