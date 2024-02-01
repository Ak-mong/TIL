import sys; sys.stdin = open('../txt/4direction.txt')

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # print(arr)
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    total = 0
    # 2차원 배열 순회 : 2중 for + 4방향 for = for문 3중첩
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 인덱스체크 (최우선) 벽 체크
                if 0 <= ni < n and 0 <= nj < n:
                    temp = arr[i][j] - arr[ni][nj]
                    if temp >= 0:
                        total += temp
                    else:
                        total += temp * -1
    print(f'#{tc} {total}')