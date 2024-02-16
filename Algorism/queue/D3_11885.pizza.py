import sys; sys.stdin = open('txt/pizza.txt')
#N개의 피자
# 1~M+1
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    num_arr = []
    for i in range(M):
        num_arr.append([arr[i],i])
    oven = []
    for i in range(N):
        oven.append(num_arr[i])
    # print(oven)
    rear = -1
    cnt = 0
    while True:
        rear += 1
        oven[rear%N][0] = oven[rear%N][0] // 2
        if oven[rear % N][0] == 0:
            oven.pop(rear % N) # 오븐의 인덱스를 pop
            if N+cnt < M:
                oven.insert(rear % N,num_arr[N+cnt]) # 오븐의 인덱스에 insert
                cnt += 1
            else: #뽑을게 없다
                oven.append([-1,-1])
        if oven.count([-1,-1]) == N-1:
            break
    print(f'#{tc} {oven[0][1]+1}')

