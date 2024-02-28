import sys;
sys.stdin =open('input.txt')

# t = int(input())
# for tc in range(t):
c,r = map(int,input().split()) # 가로 세로
k = int(input()) # 총 시행 횟수
arr = [[0]*(r+1) for _ in range(c+1)]
dij = [[0,1],[1,0],[0,-1],[-1,0]] # 오 아 왼 위
def find_seat():
    if k > r*c: #예외처리
        return
    move = 0
    idx = 1
    i,j = 1,1
    while idx <= k:
        arr[i][j] = idx
        ni = i + dij[move%4][0]
        nj = j + dij[move%4][1]
        if 0< ni<= c and 0< nj <= r and arr[ni][nj] == 0:
            i,j = ni,nj
        else:
            move += 1  # 방향 바꾸기
            i, j = i + dij[move % 4][0], j + dij[move % 4][1]

        idx += 1
def find_xy():
    for i in range(c+1):
        for j in range(r+1):
            if arr[i][j] == k:
                return i,j
    return 0,
find_seat()
print(*find_xy())