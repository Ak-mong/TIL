import sys; sys.stdin = open('txt/ballon.txt')
di = [0,1,0,-1]
dj = [1,0,-1,0]
t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    ballon_list = [list(map(int, input().split())) for _ in range(n)]
    max_v = 0 # 한 지점을 확인할 때 마다 초기화한다.
    for i in range(n):
        for j in range(m):
            pop_num = ballon_list[i][j]
            for k in range(4): # 4방향 탐색을 하겠다
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<n and 0<=nj<m: # 벽 체크
                    pop_num += ballon_list[ni][nj]
            if max_v < pop_num: # 4방향 탐색이 끝나고 나서 이전 지점과의 최대값을 비교한다.
                max_v = pop_num
    print(f'#{tc} {max_v}') # 모든 지점에 대한 탐색(한 case)이 끝난 후 최대값을 출력한다.
