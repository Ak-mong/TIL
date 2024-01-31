import sys;sys.stdin = open("txt/4direction.txt", "r")
T = int(input())
def abs_v(arr1, arr2):
    value = 0
    if arr1 >= arr2:
        value = arr1 - arr2
    else:
        value = arr2 - arr1
    return value
di = [0, 1, 0, -1]
dj = [1, 0 ,-1, 0]
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum += abs_v(arr[i][j], arr[ni][nj])
    print(f'#{tc} {sum}')
