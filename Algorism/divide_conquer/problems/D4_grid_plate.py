import sys;sys.stdin =open('grid_plate.txt','r')

di = [0,1,0,-1]
dj = [1,0,-1,0]


def dfs(y,x, path):
    # 기저 조건 : 7 자리면 끝
    if len(path) == 7:
        # 현재까지의 경로를 저장
        result.add(path)
        return

    for i in range(4):
        new_y = y + di[i]
        new_x = x + dj[i]

        # 범위 밖으로 넘어가면 pass
        if new_y < 0 or new_y >= 4 or new_x < 0 or new_x >=4: continue
        dfs(new_y,new_x, path + maps[new_y][new_x])

t = int(input())
for tc in range(1,t+1):
    # maps = [list(map(int,input().split())) for _ in range(4)]

    # 갈 때 마다 경로를 더하기 위해서 문자열로 저장
    maps = [input().split() for _ in range(4)]
    print(maps)

    # 중복을 제거하기 위한 set 사용
    result = set()
    path = []
    # 시작 지점
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])

    print(f'#{tc} {len(result)}')