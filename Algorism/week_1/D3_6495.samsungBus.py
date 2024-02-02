import sys; sys.stdin = open('txt/samsungBus.txt')

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    # a , b = [map(int,input().split()) for _ in range(n)]
    cnt = [0] * 5001
    for i in range(n):
        a, b = map(int,input().split())
        for j in range(a,b+1):
            cnt[j] +=1
    p = int(input())
    bus_stop = [int(input()) for _ in range(p)]
    print(f'#{tc}',end=' ')
    for k in bus_stop: #정류장 별로 cnt 갯수 출력 = 노선을 지나가는 버스 수
        print(cnt[k], end=' ')
    print()

