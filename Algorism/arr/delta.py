di =  [0, 1, 0, -1] # 방향별로 더할 값
dj =  [1, 0, -1, 0]
N =5
arr = [[0]*N for _ in range(N)]
for i in range(N): # 행
    for j in range(N): # 열
        print('갈 수 있는 방향', end=' ')
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # print(arr[ni][nj], end = ' ')
                print(f' ({i},{j})->({ni},{nj})', end = ' ')
        #     print((ni, nj), end=' ')
        print()
# i = 3
# j = 4
