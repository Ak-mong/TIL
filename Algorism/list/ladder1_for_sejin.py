for _ in range(10):
    test_case = int(input())

    # 도착지점은 맨 아랫줄에 2로 표시되어 있어서
    # 먼저 도착지점부터 찾고 거기서 위로 출발해서 델타 탐색
    ladder = [0] * 100
    for i in range(100):
        ladder[i] = list(map(int, input().split()))

    # 1. 왼쪽, 2. 오른쪽, 3. 위쪽 순서로 탐색
    dx = [-1, 1, 0]
    dy = [0, 0, -1]

    x = None
    y = 99
    # 도착 지점 찾기
    for i in range(100):
        if ladder[y][i] == 2:
            x = i
            break

    # 지나갔던 길은 0으로 만들어줌
    while y > 0:
        for k in range(3):
            x_dx = x + dx[k]
            y_dy = y + dy[k]
            if 0 <= x_dx < 100 and 0 <= y_dy < 100:
                if ladder[y_dy][x_dx] == 1:
                    x = x_dx
                    y = y_dy
                    break
        ladder[y][x] = 0
    print(f'#{test_case} {x}')