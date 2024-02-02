import sys; sys.stdin = open('txt/ballon.txt')
di = [0,1,0,-1]
dj = [1,0,-1,0]
t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    ballon_list = [list(map(int,input().split())) for _ in range(n)]
    # 한 케이스마다 돌리기 및 최대값 초기화
    max_v = 0
    for i in range(n):
        for j in range(m):
            # 한 지점에서 터진 갯수 초기화
            cnt = ballon_list[i][j]
            # 4방향 탐색
            for k in range(4):
                for p in range(1, ballon_list[i][j]+1): # 4개라면 1 2 3 4만큼 더 가서 터트린다.
                    ni = i + di[k]*p
                    nj = j + dj[k]*p
                    if 0<=ni<n and 0<=nj<m: # 실수한 곳!! nj는 m으로 돌아야된다.
                        # 실수한곳!!!! cnt += 1 # 1개 더 가서 1추가 2개 더가서 1추가 ...
                        cnt += ballon_list[ni][nj] # 해당 풍선의 꽃가루 수만큼 터져나감
            # 4방향 탐색이 끝난 후 최대값 비교
            if max_v < cnt:
                max_v = cnt
                # print(max_v)
    print(f'#{tc} {max_v}')
