import sys; sys.stdin = open('../txt/samsungBus.txt')

t = int(input())
for tc in range(1,t+1):
    n= int(input())
    counts = [0] * 5001 # 5000번 정류장
    # N 개의 노선을 정류장에 표시
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a,b+1): # 1 <= a <= b <= 5000
            counts[j] += 1
    p = int(input())
    busstop = [int(input()) for _ in range(p)]
    print(f'#{tc}' , end= ' ')
    for i in busstop: #출력할 정류장
        print(counts[i], end= ' ')
    print()