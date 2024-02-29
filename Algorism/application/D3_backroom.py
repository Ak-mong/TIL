import sys;sys.stdin = open('txt/back_room.txt')
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    count = [0] * 401
    max_v = 0

    arr = []
    for _ in range(n):
        arr.append(tuple(map(int, input().split())))

    for x in arr:
        # 현재방 s, 돌아갈 방 e
        s, e = x
        # 아랫방을 윗방으로 변경
        if s%2 ==0: s -= 1
        if e%2 ==0: e -= 1

        # 출발지보다 목적지가 더 큰 값이 되도록 swap
        if s > e: s, e = e, s # swap
        for i in range(s,e+1):
            count[i] += 1
            max_v = max(count[i], max_v)
    print(count)
    print(f'#{tc} {max_v}')


    count1 = [0] * 401

    for i in arr:
        s,e = i
        if s > e: s, e = e, s  # swap
        for j in range(s,e+1):
            count1[j] +=1

    print(count1)
    print(f'#{tc} {max(count1)}')
    print('다음')
