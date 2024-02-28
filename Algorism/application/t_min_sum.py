import sys;sys.stdin = open('txt/min_sum.txt')
import time
start_time = time.time()
drc = [[0,1],[1,0]] # 오 아
def gogo(r,c,s): # 행, 열 , 합
    global min_v
    if s > min_v: # 가지치기
        return
    if r == n-1 and c == n-1:
        # print(s)
        if min_v > s:
            min_v = s
        return
    for k in range(2):
        nr = r + drc[k][0]
        nc = c + drc[k][1]
        if 0 <= nr < n and 0 <= nc < n: # 벽체크
            # min_v += arr[nr][nc]
            gogo(nr,nc,s + arr[nr][nc])
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # print(arr)
    min_v = 1000000000000000
    gogo(0,0,arr[0][0]) # 시작좌표 값 넣기
    print(f'#{tc} {min_v}')
print(f'{start_time - time.time():.10f}')
