import sys
sys.stdin = open('../txt/ladder1.txt')
# sys.stdin = open('../txt/ladder1_out.txt','w') # 출력된것을 확인하기 위해 사용할 수 있음
dr = [0,0,-1] #왼 오 위
dc = [-1,1,0]
t = 10
n = 100
def find_position(arr):
    for i in range(n):
        if arr[n-1][i] == 2:
            return n-1, i #(r,c)
def ladder(arr,r,c):
    while True:
        # 제일 위쪽행에 도착하면 그때 열을 리턴
        if r == 0: return c
        # 3방향 탐색
        for k in range(3):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 1:
                r, c = nr, nc
                arr[r][c] = 9 #방문체크 한번만 타기 때문에 9로 둘 수 있었음

for tc in range(1, t+1):
    # 밑에서 부터 올라가는걸 찾자
    no = input()
    ladder_list = [list(map(int, input().split())) for _ in range(n)]
    r,c = find_position(ladder_list) # 2인 시작위치 찾기
    print(f'#{tc} {ladder(ladder_list,r,c)}')
    # for i in ladder_list:
    #     print(*i)